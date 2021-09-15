from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from src.oauth.services.google import check_google_auth

from .. import serializers


def google_login(request):
    '''
    enter via google
    '''
    return render(request, 'oauth/google_login.html')



@api_view(['POST'])
def google_auth(request):
    '''
    Confirmation data from google
    '''
    google_data = serializers.GoogleAuth(data=request.data)
    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response(token) 
          
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')