from django import forms
from .models import Patient, Test, Payment, Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_num', 'address', 'email']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_name', 'test_date', 'result']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_date']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_name', 'content']

class signup(UserCreationForm):
    uname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = ('uname', 'email', 'password1','password2')

    def save(self,commit = True):
        user = super(signup,self).save(commit = False)
        user.uname = self.cleaned_data['uname']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

