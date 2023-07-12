from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    contact_num = models.IntegerField()
    address = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Test(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient.name} - {self.test_name}"


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.patient.name} - {self.amount}"


class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.report_name}"

    def login(self):
        return self.login

    def signup(self):
        return self.signup
