import datetime
from django.db import models

class Chemicals(models.Model):
	iupac_name = models.CharField(max_length=100)
	manufacturer = models.CharField(max_length=100)
	data_enter = models.DateField(auto_now=True)
	data_expire = models.DateField()
	chem_status = models.BooleanField(default=True)

	def __str__(self):
		return self.iupac_name

class Glassware(models.Model):
	glassware_name = models.CharField(max_length=50)
	volume = models.CharField(max_length=25)
	grade = models.CharField(max_length=2)
	quantity = models.IntegerField()
	data_enter = models.DateField(auto_now=True)
	manufacturer = models.CharField(max_length=100)



