from __future__ import unicode_literals

from django.apps import AppConfig


class FeaturesConfig(AppConfig):
    name = 'service.features'

    def ready(self):
        from . import signals
