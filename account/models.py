from django.db import models

# Create your models here.

class User(models.Model):

    USER_TYPES = (('user', 'User'), ('admin', 'Admin'))

    user_name = models.CharField (max_length = 30, unique = True)

    password = models.CharField (max_length = 256)

    email = models.EmailField (max_length = 100, null = True, blank = True)

    user_type = models.CharField (max_length = 10, choices = USER_TYPES, default = 'user')

    last_login = models.DateTimeField (null = True, blank = True)

    created_at = models.DateTimeField (auto_now_add = True)

    modified_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.user_name