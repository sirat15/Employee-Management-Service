from rest_framework import serializers
from .models import Employee , Team , WorkArr

class WorkArrSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArr 
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
         model = Team
         fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
'''
class Team_LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Leader
        fields = '__all__'
        '''


