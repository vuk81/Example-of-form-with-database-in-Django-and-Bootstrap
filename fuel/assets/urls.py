from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'assets'
urlpatterns = [
    path('chemicals', views.chemicals_list, name='chemicals'),
    path('glassware', views.glassware_list, name='chemicals'),
    path('chemicals/delete/<int:chem_id>', views.chemicals_delete, name='chem_delete'),
    path('glassware/delete/<int:glass_id>', views.glassware_delete, name='glass_delete'),

]
