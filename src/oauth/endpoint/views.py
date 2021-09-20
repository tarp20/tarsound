from rest_framework import parsers, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from src.oauth.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    '''
    Viewing and editing user data
    '''
    parser_classes = (parsers.MultiPartParser, )
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()

    
