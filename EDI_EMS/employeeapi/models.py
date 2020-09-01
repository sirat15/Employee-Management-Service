from django.db import models

# Create your models here.
class WorkArr(models.Model):
    WorkType = models.CharField(max_length=50)

    def __str__(self):
        return self.WorkType

class TeamID(models.Model):
    TeamName = models.CharField(max_length=100)

    def __str__(self):
        return self.TeamName
    

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    team = models.ForeignKey(TeamID, on_delete=models.CASCADE)
    employment_type = models.ForeignKey(WorkArr, on_delete= models.CASCADE)
    hourly_rate = models.IntegerField(default = 10, editable = False)

    





#class TeamLeader(models.Model):
#    TeamLeaderID = models.ForeignKey(Employee, on_delete=models.CASCADE)

#class WorkArrangement(models.Model):
#    WorkType = models.CharField(max_length=50)



