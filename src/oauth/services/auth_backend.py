from datetime import datetime

import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from src.oauth.models import AuthUser


class AuthBackend(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request, *args, **kwargs):
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header or auth_header[0].lower() != b'token':
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. No credential provided.')
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token string should not contain spaces')

        try:
            token = auth_header[1].decode('utf-8')
        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token String should not contain invalid characters.'
            )

        return self.authenticate_credential(token)

    def authenticate_credential(self, token):
        try:
            payload = jwt.decode(token,
                                 settings.SECRET_KEY,
                                 algorithm=settings.ALGORITHM)
        except jwt.PyJWKError:
            raise exceptions.AuthenticationFailed(
                'Invalid authentication. Could not decode token: %s' % token)

        token_exp = datetime.fromtimestamp(payload['exp'])
        if token_exp < datetime.utcnow():
            raise exceptions.AuthenticationFailed('Token Expired')

        try:
            user = AuthUser.objects.get(id=payload['user_id'])
        except AuthUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'No user matching this token was found.')

        return user, None
