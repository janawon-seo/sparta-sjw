from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField("핸드폰 번호", max_length=12)
    address = models.TextField("주소")
