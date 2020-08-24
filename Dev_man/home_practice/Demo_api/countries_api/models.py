from django.db import models

# Create your models here.
class Countries(models.Model):
	name = models.CharField(max_length=20, blank=False, null=False)
	capital = models.CharField(max_length=50, blank=False, null=False, default='')