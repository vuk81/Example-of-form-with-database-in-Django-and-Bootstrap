from django.forms import ModelForm
from .models import Chemicals, Glassware

class newChemical(ModelForm):
	class Meta:
		model = Chemicals
		exclude = ['chem_status']
    
class newGlassware(ModelForm):
	class Meta:
		model = Glassware
		ordering = ['glassware_name']
		exclude =[]