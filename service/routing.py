from channels import route
from .features import consumers

path = r'^/api/projects/(?P<pk>\d+)/stream/$'

channel_routing = [
    route("websocket.connect", consumers.connect_to_project, path=path),
    route("websocket.receive", consumers.disconnect_from_project, path=path)
]