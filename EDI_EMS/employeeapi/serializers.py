from rest_framework import serializers
from .models import Employee , TeamID , WorkArr

class WorkArrSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArr 
        fields = '__all__'

class TeamIDSerializer(serializers.ModelSerializer):
    class Meta:
         model = TeamID
         fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



#class TeamLeaderSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = TeamLeader
#        fields = '__all__'        

