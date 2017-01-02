from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Project
from service.features.tasks import create_keys_for_project, import_features_from_git_repo


@receiver(post_save, sender=Project)
def handle_new_project(sender, instance, created, **kwargs):
    if created and instance.repo_url:
        create_keys_for_project.delay(instance.id)
