from rest_framework_jwt.utils import jwt_payload_handler as default_jwt_payload_handler


def jwt_payload_handler(user=None):
    payload = default_jwt_payload_handler(user)
    payload['is_staff'] = user.is_staff
    return payload