from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class custom_user(AbstractUser):
    # 1 -> usuario
    # -> criador
    tipo = models.IntegerField(default=1)
    pass
