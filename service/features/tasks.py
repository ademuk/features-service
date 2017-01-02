from __future__ import absolute_import

from celery import shared_task

from .models import Project


@shared_task
def import_features_from_git_repo(project_id):
    project = Project.objects.get(pk=project_id)

    print('%s - Importing features from: %s' % (project.name, project.repo_url))

    project.import_features_from_git()


@shared_task
def create_keys_for_project(project_id):
    project = Project.objects.get(pk=project_id)

    print('%s - Creating keys' % project.name)

    project.create_keys()
