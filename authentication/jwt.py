from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
import jwt
from authentication.models import User


class JWTAuthentication(BaseAuthentication):


    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        utilisateur = 'vide'
        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')
        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            username = payload['username']
            user = User.objects.get(username=username)
            utilisateur=payload['username']

            return user, token

        except jwt.ExpiredSignatureError as expErr:
            raise exceptions.AuthenticationFailed('Token is expired, login again')
        except jwt.DecodeError as decoErr:
            raise exceptions.AuthenticationFailed('The token might be invalid {}'.format(utilisateur))
        except User.DoesNotExist as userExError:
            raise exceptions.AuthenticationFailed('This user does not exist')










