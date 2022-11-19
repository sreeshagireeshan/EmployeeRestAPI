from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_salary=models.PositiveIntegerField()
    emp_age=models.PositiveIntegerField()
    emp_city=models.CharField(max_length=20)
    
