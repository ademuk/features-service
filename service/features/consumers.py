from channels import Group
from .models import Project


def connect_to_project(message, pk):
    message.reply_channel.send({"accept": True})

    project = Project.objects.get(pk=pk)

    Group('project-%d' % project.id).add(message.reply_channel)


def disconnect_from_project(message, pk):
    project = Project.objects.get(pk=pk)

    Group('project-%d' % project.id).discard(message.reply_channel)