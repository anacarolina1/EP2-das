from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from ep2Site.models import Review
import os.path
from djangoplugins.signals import django_plugin_disabled, django_plugin_enabled

@receiver(django_plugin_enabled)
def _django_plugin_enabled(sender, plugin, **kwargs):
    enable_plugin(plugin)

    @receiver(django_plugin_disabled)
    def _django_plugin_disabled(sender, plugin, **kwargs):
        disable_plugin(plugin)

@receiver(post_save, sender=Review)
def model_post_save(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
 
 
@receiver(post_delete, sender=Review)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))
 
 
