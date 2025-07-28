from django.contrib.auth.models import User
from django.db import models

class PasswordHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashed_password = models.CharField(max_length=255)
    changed_at = models.DateTimeField(auto_now_add=True)
