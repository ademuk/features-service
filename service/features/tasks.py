from __future__ import absolute_import

from celery import shared_task

from .models import Project


@shared_task
def import_features_from_repo(project_id):
    project = Project.objects.get(pk=project_id)

    print('%s - Importing features from: %s' % (project.name, project.repo_url))

    project.import_features_from_repo()

