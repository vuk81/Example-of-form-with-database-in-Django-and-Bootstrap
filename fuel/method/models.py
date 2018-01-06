from django.db import models

class Method(models.Model):
	standard = models.CharField(max_length=10)
	standard_title = models.CharField(max_length=250)
	intro = models.CharField(max_length=500)
	repeatibility = models.FloatField()
	repoducibility = models.FloatField()	
