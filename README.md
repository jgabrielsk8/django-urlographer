django-urlographer
==================

A URL mapper for the django web framework

[![Build Status](https://travis-ci.org/ConsumerAffairs/django-urlographer.png?branch=master)](https://travis-ci.org/ConsumerAffairs/django-urlographer)
[![Coverage Status](https://coveralls.io/repos/ConsumerAffairs/django-urlographer/badge.png)](https://coveralls.io/r/ConsumerAffairs/django-urlographer)

Features:

* supplements the django url resolution
* database + cache driven
* automatic caching and cache invalidation on save
* permanent and temporary redirects
* map url to arbitrary status code
* url canonicalization
    * lowercase
    * ascii
    * eliminate relative paths
    * extra slashes
