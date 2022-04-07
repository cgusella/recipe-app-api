from rest_framework import generics
from user.serializers import UserSerializer
from user.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import authentication
from rest_framework import permissions


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


# IMPORTANT: use the RetrieveUpdateApiView to let the patch method works.
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
        # So when the object is called the request will have the user
        # attached to it because of the authentication classes.
