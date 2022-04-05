from distutils.command.upload import upload
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'