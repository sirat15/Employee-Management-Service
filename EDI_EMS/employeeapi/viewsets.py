from rest_framework import viewsets
from . import models
from . import serializers

# internally create few classes like create(), lists(), update() etc.

class WorkArrViewset(viewsets.ModelViewSet):
    queryset = models.WorkArr.objects.all()
    serializer_class = serializers.WorkArrSerializer

class TeamIDViewset(viewsets.ModelViewSet):
    queryset = models.TeamID.objects.all()
    serializer_class = serializers.TeamIDSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    for record in queryset:
        record.update_salary()
    #result = models.Employee.objects.filter().values('fullname','salary')
    serializer_class = serializers.EmployeeSerializer

'''class TeamLeaderViewset(viewsets.ModelViewSet):
    queryset = models.TeamLeader.objects.all()
    serializer_class = serializers.TeamLeaderSerializer    '''