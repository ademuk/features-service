from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class JSONWebTokenCsrfExemptAuthentication(JSONWebTokenAuthentication):

    def enforce_csrf(self, request):
        return
