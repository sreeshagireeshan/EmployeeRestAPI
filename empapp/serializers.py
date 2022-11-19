from rest_framework import serializers
from .models import *
class EmployeeDetailsSerializers(serializers.ModelSerializer):
    emp_name=serializers.CharField(max_length=20)
    emp_salary=serializers.IntegerField()
    emp_age=serializers.IntegerField()
    emp_city=serializers.CharField(max_length=20)

    class Meta:
        model=EmployeeDetails
        fields=('__all__')
