from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # urls for authentication
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),

    # urls for Incidents
    path('Incidents', views.Incidents, name='Incidents'),
    path('IncidentView/<id>', views.IncidentView, name='IncidentView'),
    path('Incidentdelet/<id>', views.Incidentdelet, name="Incidentdelet"),
    path('Incidentcreate/', views.Incidentcreate, name="Incidentcreate"),
    path('Incidentedit/<id>', views.Incidentedit, name="Incidentedit"),
    path('Incidentedit/saveIncidentedit/<id>', views.saveIncidentedit, name="saveIncidentedit"),
]