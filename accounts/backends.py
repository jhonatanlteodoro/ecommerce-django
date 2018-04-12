from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model

class ModelBackend(BaseModelBackend):

    def authenticate(self, username=None, password=None):
        if not username is None:
            usermodel = get_user_model()
            try:
                user = usermodel.objects.get(email=username)
                if user.check_password(password):
                    return user
            except usermodel.DoesNotExist as e:
                pass
