# coding: utf-8
from django import forms
from django.contrib import admin
from django.contrib.sites.models import Site
from urlographer.models import URLMap, ContentMap


SQL_COUNT_REDIRECTS = """
SELECT count(map2.id)
FROM urlographer_urlmap map2
WHERE map2.status_code=301
AND map2.redirect_id=urlographer_urlmap.id"""


class HasRedirectsToItListFilter(admin.SimpleListFilter):
    title = 'has redirects to it'
    parameter_name = 'has_redirects_to_it'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        join_sql = SQL_COUNT_REDIRECTS
        if self.value() == 'yes':
            return queryset.extra(where=["(%s)>0" % join_sql])
        if self.value() == 'no':
            return queryset.extra(where=["(%s)=0" % join_sql])


class SiteModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{0}".format(obj.name)


class URLMapAdminForm(forms.ModelForm):

    site = SiteModelChoiceField(queryset=Site.objects.all())

    class Meta:
        model = URLMap
        exclude = ()


class URLMapAdmin(admin.ModelAdmin):
    form = URLMapAdminForm

    def queryset(self, request):
        # Rename to `get_queryset` in Django version > 1.5
        return super(URLMapAdmin, self).queryset(request).extra(select={
            'redirects_count': SQL_COUNT_REDIRECTS
        })

    def redirects_count(self, obj):
        return obj.redirects_count

    list_display = (
        'id',
        'path',
        'content_map',
        'status_code',
        'on_sitemap',
        'created',
        'redirects_count')
    list_filter = (
        'status_code',
        'on_sitemap',
        ('created', admin.DateFieldListFilter),
        HasRedirectsToItListFilter)
    raw_id_fields = ('redirect', 'content_map')
    readonly_fields = ('hexdigest',)
    search_fields = ('path',)


admin.site.register(URLMap, URLMapAdmin)
admin.site.register(ContentMap)
