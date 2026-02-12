from django.contrib.auth.models import User

class UserService:
    def register_user(self, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        return user
