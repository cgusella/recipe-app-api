from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    # DO NOT CLOSE THE EQUIVALENCE BELOW WITH BRACKETS.
    # Or: do not write
    #   serializer_class = UserSerializer()
    # or the compiler will give you the 'not callable error'.
    # And it's right, as it is an instance written this way.
    serializer_class = UserSerializer
