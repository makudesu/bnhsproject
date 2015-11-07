from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_TYPE, null=False)
    date_of_birth = models.DateField(null=True)

    def __unicode__(self):
        return self.email
