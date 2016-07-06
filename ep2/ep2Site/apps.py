from django.apps import AppConfig


class Ep2SiteConfig(AppConfig):
    name = 'ep2Site'
    verbose_name = 'ep2Site Application'

    def ready(self):
        import ep2Site.signals


