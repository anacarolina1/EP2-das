from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from models import Review
import os.path

@receiver(post_save, sender=Review)
def model_post_save(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
 
 
@receiver(post_delete, sender=Review)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))
