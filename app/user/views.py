from rest_framework import generics
from user.serializers import UserSerializer
from user.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    # DO NOT CLOSE THE EQUIVALENCE BELOW WITH BRACKETS.
    # Or: do not write
    #   serializer_class = UserSerializer()
    # or the compiler will give you the 'not callable error'.
    # And it's right, as it is an instance written this way.
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new authtoken for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # For this last one see the documentation:
    # https://www.django-rest-framework.org/api-guide/settings/#api-reference
