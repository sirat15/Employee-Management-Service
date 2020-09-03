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
    hourly_rate = models.IntegerField()
    salary = models.IntegerField(default = 10)

    def update_salary(self):
        #teamObj=TeamID.objects.get(self.teamId)
        if self.employment_type == 1:
            self.salary = self.hourly_rate * 160
        else:
            self.salary = self.hourly_rate * 120
        #if teamObj.teamLeaderId == self.id
        #    self.salary = self.salary*1.1
        self.save()
        return self.salary    

    def __str__(self):
        return self.fullname


