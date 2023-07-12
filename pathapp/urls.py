from django.urls import path
from . import views

urlpatterns = [
    path('p_create', views.create_patient, name='create_patient'),
    path('patients/update/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', views.patient_details, name='patient_details'),
    path('patients/<int:patient_id>/tests/create/', views.create_test, name='create_test'),
    path('patients/<int:patient_id>/payments/create/', views.create_payment, name='create_payment'),
    path('patients/<int:patient_id>/reports/create/', views.create_report, name='create_report'),
]
