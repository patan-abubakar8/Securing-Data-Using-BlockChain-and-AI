from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the root path
    path("index.html", views.index, name="index"),  # URL for index.html without the root path
    path("CreateProfile.html", views.CreateProfile, name="CreateProfile"),
    path("CreateProfileData", views.CreateProfileData, name="CreateProfileData"),
    path("Hospital.html", views.Hospital, name="Hospital"),
    path("HospitalLogin", views.HospitalLogin, name="HospitalLogin"),
    path("AccessData.html", views.AccessData, name="AccessData"),
    path("PatientDataAccess", views.PatientDataAccess, name="PatientDataAccess"),
    path("Patient.html", views.Patient, name="Patient"),
    path("PatientLogin", views.PatientLogin, name="PatientLogin"),
]

