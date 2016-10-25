from __future__ import unicode_literals
import json

from django.db import models

from channels import Group

from .importer import GitFeatureImporter


class Project(models.Model):
    STATUS_ADDING = 'adding'
    STATUS_ADDED = 'added'
    STATUS_ADDING_ERROR = 'adding_error'
    STATUS_CHOICES = (
        (STATUS_ADDING, 'Adding'),
        (STATUS_ADDED, 'Added'),
        (STATUS_ADDING_ERROR, 'Adding Error')
    )

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_ADDED)
    users = models.ManyToManyField('auth.User', related_name='projects', blank=True)
    repo_url = models.CharField(max_length=255, blank=True)
    features_path = models.CharField(max_length=255, blank=True)

    def import_features_from_git(self):
        importer = GitFeatureImporter(self)

        try:
            self.features_path = importer.run()
            self.set_status(Project.STATUS_ADDED)
        except:
            self.set_status(Project.STATUS_ADDING_ERROR)

        self.save()

    def set_status(self, status):
        self.status = status

        Group('project-%d' % self.id).send({
            'text': json.dumps({
                'status': self.status
            })
        })

    def __str__(self):
        return self.name


class Feature(models.Model):
    project = models.ForeignKey(Project, related_name='features')
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name