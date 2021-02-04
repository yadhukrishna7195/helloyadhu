from django.db import models
import datetime

# Create your models here.


class Contact(models.Model):

    name = models.CharField(null=True,blank=True, max_length=50)
    phone = models.CharField(null=True,blank=True, max_length=50)
    email = models.CharField(null=True,blank=True, max_length=50)
    subject = models.CharField(null=True,blank=True, max_length=150)
    message = models.CharField(null=True,blank=True, max_length=150)
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return u'{0}'.format(self.name)
