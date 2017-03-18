from channels import route
from .features import consumers

path = r'^/api/projects/(?P<id>[0-9a-f-]+)/stream/$'

channel_routing = [
    route("websocket.connect", consumers.connect_to_project, path=path),
    route("websocket.receive", consumers.disconnect_from_project, path=path)
]
