from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, FeatureDetailView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^features/(?P<id>[0-9a-f-]+)/?$', FeatureDetailView.as_view(), name='feature-detail')
]
