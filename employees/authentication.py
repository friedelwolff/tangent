
from django.contrib.auth.models import User

class WebServiceAuthentication:

    def authenticate(self, request, username=None, password=None):
        if not (username and password):
            return None

        # Create an internal user for each remote user. This way we can easily
        # use the session, etc.
        user, created = User.objects.get_or_create(username=username)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
