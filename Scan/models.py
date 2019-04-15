from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter

# Create your models here.
class Website(models.Model):
    """
    Model representing a website stat
    """
    #name = models.CharField(max_length=200)
    URL = models.TextField(max_length=400)
    # Store the URL of the website
    lastchecked = models.DateField()
    #when was the website entry last updated in the database.
    sql_i_score = models.BooleanField()
    #score = models.IntegerField()
    # the number of vulnerabilities that were found in the website the last time

    class Meta:
        ordering = ["name"]
