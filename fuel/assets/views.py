import datetime
from django.shortcuts import render, redirect
from .models import Chemicals, Glassware
from .forms import newChemical, newGlassware


def chemicals_list(request):
	chem = {}
	expire = {}
	if request.method == 'POST':
		form = newChemical(request.POST)
		if form.is_valid():
			form.save()
			chem = Chemicals.objects.all()
	else:
		form = newChemical()
		chem = Chemicals.objects.all()
	
	return render(request, 'chemicals/chemicals.html', {'form': form, 'chem': chem})

def chemicals_delete(request, chem_id):
	chem = Chemicals.objects.get(id=chem_id).delete()
	
	return redirect('/assets/chemicals')




def glassware_list(request):
	glass = {}
	if request.method == 'POST':
		form = newGlassware(request.POST)
		if form.is_valid():
			form.save()
			glass = Glassware.objects.all()
	else:
		form = newGlassware()
		glass = Glassware.objects.all()

	return render(request, 'glassware/glassware.html', {'form': form, 'glass': glass})

def glassware_delete(request, glass_id):
	glass = Glassware.objects.get(id=glass_id).delete()
	
	return redirect('/assets/glassware')
