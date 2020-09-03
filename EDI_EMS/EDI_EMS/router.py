from employeeapi.viewsets import EmployeeViewset , TeamIDViewset , WorkArrViewset 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)

router.register('team',TeamIDViewset)
router.register('workarr',WorkArrViewset)
#router.register('teamlead',TeamLeaderViewset)

#Function which will check passcode then fetch data fromDB and calculate salary and then send response with employeename.