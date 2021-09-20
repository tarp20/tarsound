from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')

class GoogleAuth(serializers.Serializer):
    '''
    Serialization data from Google
    '''

    email = serializers.EmailField()
    token = serializers.CharField()