from django.test import TestCase
from employeeapi.models import WorkArr , Employee , Team
from employeeapi.viewsets import EmployeeViewset , TeamViewset , WorkArrViewset 

# first failed test
'''class TestModel(TestCase):

    def test_string_representation(self):
        self.fail("Test incomplete") '''
# to check the __str__ method in WorkArr Model
class TestWorkArrModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        WorkArr.objects.create(WorkType='Intern')

    def test_string_representation(self):
        workarr = WorkArr.objects.get(id=1)
        field_label = workarr._meta.get_field('WorkType').verbose_name
        self.assertEquals(field_label, 'WorkType')        

# to check the __str__ method in Team Model
class TestTeamModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.create(TeamName = 'Finance',TeamLeaderId = 1)
        

    def test_string_representation(self):
        team = Team.objects.get(id=1)
        field_label = team._meta.get_field('TeamLeaderId').verbose_name
        self.assertEquals(field_label, 'TeamLeaderId') 