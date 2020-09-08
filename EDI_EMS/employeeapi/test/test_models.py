from django.test import TestCase
from employeeapi.models import WorkArr , Employee , Team
from employeeapi.viewsets import EmployeeViewset , TeamViewset , WorkArrViewset 

# first failed test
class TestModel(TestCase):

    def test_string_representation(self):
        self.fail("Test incomplete") 

