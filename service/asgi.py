# asgi.py

import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

channel_layer = get_channel_layer()