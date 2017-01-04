from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Project, Feature
from .serializers import ProjectSerializer, FeatureSerializer
from service.features.tasks import import_features_from_repo


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user.projects.all()

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user]).status

    @detail_route(methods=['post', 'get'])
    def features(self, request, pk=None):
        project = self.get_object()
        if request.method == "POST":
            project.set_status(Project.STATUS_IMPORTING)
            import_features_from_repo.delay(project.id)
            return Response({}, status=status.HTTP_202_ACCEPTED)
        else:
            queryset = project.features.all()
            serializer = FeatureSerializer(queryset, many=True)
            return Response(serializer.data)


class FeatureDetailView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Feature.objects.filter(project__in=user.projects.all())
