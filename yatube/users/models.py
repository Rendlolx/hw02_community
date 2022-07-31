from django.db import models

# Create your models here.
class ChangePasswordAfterReset(models.Model):
    new_pass = models.CharField(max_length=40)
    new_pass_confirm = models.CharField(max_length=40)
    