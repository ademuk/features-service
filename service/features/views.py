from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Project, Feature
from .serializers import ProjectSerializer, FeatureSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user.projects.all()

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user]).status

    @detail_route()
    def features(self, request, pk=None):
        project = self.get_object()
        queryset = project.features.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)


class FeatureDetailView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Feature.objects.filter(project__in=user.projects.all())
