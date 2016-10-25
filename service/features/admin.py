from django.contrib import admin
from .models import Project, Feature


class ProjectAdmin(admin.ModelAdmin):
    pass


class FeatureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feature, FeatureAdmin)