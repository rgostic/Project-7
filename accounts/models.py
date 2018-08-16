from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, default="")
	last_name = models.CharField(max_length=100, default="")
	email = models.EmailField(default="")
	birthday = models.DateField(null=True, blank=True)
	bio = models.TextField(default="")
	avatar = models.ImageField(null=True, blank=True)

	