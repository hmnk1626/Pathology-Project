from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Test, Payment, Report
from .forms import PatientForm, TestForm, PaymentForm, ReportForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import signup

# View for creating a new patient
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})

# View for updating a patient
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html', {'form': form, 'patient': patient})

# View for deleting a patient
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'delete_patient.html', {'patient': patient})

# View for listing all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

# View for creating a new test for a patient
def create_test(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.patient = patient
            test.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = TestForm()
    return render(request, 'create_test.html', {'form': form, 'patient': patient})

# View for creating a new payment for a patient
def create_payment(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.patient = patient
            payment.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form, 'patient': patient})

# View for creating a new report for a patient
def create_report(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.patient = patient
            report.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = ReportForm()
    return render(request, 'create_report.html', {'form': form, 'patient': patient})

# View for displaying patient details
def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    tests = Test.objects.filter(patient=patient)
    payments = Payment.objects.filter(patient=patient)
    reports = Report.objects.filter(patient=patient)
    return render(request, 'patient_details.html', {'patient': patient, 'tests': tests, 'payments': payments, 'reports': reports})

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'post':
        username = request.post.get('username')
        password1 = request.post.get('pass')


        return redirect('home.html')

    return render(request,'login.html')

def signup(request):
    if request.method == 'post':
        form = signup(request.post)
        if form.is_valid():
            return redirect('login')
    else:
        form = signup()

    return render(request,'signup.html')
