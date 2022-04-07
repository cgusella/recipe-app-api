from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializers for the User Object"""

    class Meta:
        # Meta is a class which we use to add options at the
        # the class which is referred. For example, after we specifed the model
        # as below, UserSerializer.model will return core.user.
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
