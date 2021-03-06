from rest_framework import serializers
from .models import Project, Feature


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'status', 'repo_url', 'public_key', 'is_ssh_repo')


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id', 'name', 'body')
