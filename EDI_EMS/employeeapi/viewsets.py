from rest_framework import viewsets
from . import models
from . import serializers
#from employeeapi.MyModels import Employee_Model, Team_Model, Model_WorkArr

# internally create few classes like create(), lists(), update() etc.

class WorkArrViewset(viewsets.ModelViewSet):
    queryset = models.WorkArr.objects.all()
    serializer_class = serializers.WorkArrSerializer

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    #header accessToken=12345
    #if true
    queryset = models.Employee.objects.all()
    for record in queryset:
        record.update_salary()
    #result = models.Employee.objects.filter().values('fullname','salary')
    serializer_class = serializers.EmployeeSerializer
    #if false
    #send text contact tp your accpuntant

'''
class Team_LeaderViewset(viewsets.ModelViewSet):
    queryset = models.Team_Leader.objects.all()
    for record in queryset:
        record.Team_leader_salary()
    serializer_class = serializers.Team_LeaderSerializer'''