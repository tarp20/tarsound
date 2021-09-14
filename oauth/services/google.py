from rest_framework.exceptions import AuthenticationFailed
from oauth.serializers import GoogleAuth
from google.oauth2 import id_token
from google.auth.transport import requests


def check_google_auth(google_user: GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request())
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    #create new user or check in database
    