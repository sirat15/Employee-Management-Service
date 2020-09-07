from django.db import models

class WorkArr(models.Model):
    WorkType = models.CharField(max_length=50)

    def __str__(self):
        return self.WorkType

class Team(models.Model):
    TeamName = models.CharField(max_length=100)
    TeamLeaderId = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)
    
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    employment_type = models.ForeignKey(WorkArr,  on_delete= models.CASCADE)
    hourly_rate = models.FloatField()
    salary = models.FloatField(default = 10)
 

    def update_salary(self):
        if self.employment_type_id == 1:
            self.salary = self.hourly_rate * 160
        elif self.employment_type_id == 2:
            self.salary = self.hourly_rate * 120
        if  self.team_id_id!=0:
            teamObj=Team.objects.get(id=self.team_id_id)
            if teamObj.TeamLeaderId==self.id:
                self.salary = self.salary*1.1
        self.save()
        return self.salary   

    def __str__(self):
        return self.fullname    

    
'''class Team_Leader(models.Model):
    TeamName = models.ForeignKey('Team', on_delete=models.CASCADE)
    Team_Leader = models.ForeignKey(Employee, on_delete=models.CASCADE)
    TL_salary = models.FloatField(default = 10)

    def Team_leader_salary(self):
        self.TL_salary = Employee.objects.get('salary') * 1.1
        self.save()
        return self.TL_salary'''


