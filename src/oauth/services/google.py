from django.conf import settings

from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed

from src.oauth.models import AuthUser
from src.oauth.serializers import GoogleAuth
from src.oauth.services.base_auth import create_token


def check_google_auth(google_user: GoogleAuth) -> dict:
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request(),
                                     settings.GOOLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    #create new user or check in database
    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    return create_token(user.id)
