
from celery.task import Task

from django.db import transaction
from django.test.client import RequestFactory

from urlographer.models import URLMap
from urlographer.views import sitemap


class UpdateSitemapCacheTask(Task):

    def run(self):
        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        sitemap(request, invalidate_cache=True)


class FixRedirectLoopsTask(Task):
    """
    Task to automatically fix redirect loops.

    Example scenario:

    Before:
    A
    B
    C -> A
    D -> C -> A

    After:
    A
    B
    C -> A
    D -> A
    """

    def get_urlmaps_2_hops(self):
        qs_filters = {
            'redirect__status_code__range': (300, 399),
            'redirect__redirect__status_code__in': (200, 410)}
        return URLMap.objects.filter(**qs_filters)

    def run(self):
        for urlmap in self.get_urlmaps_2_hops():
            with transaction.atomic():
                urlmap.redirect = urlmap.redirect.redirect
                urlmap.save()
