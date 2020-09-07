from employeeapi.viewsets import EmployeeViewset , TeamViewset , WorkArrViewset 
from rest_framework import routers


router = routers.DefaultRouter()
#router.*args
#how to fetch headers in router
#header which is accessToken = something
router.register('employee',EmployeeViewset)

router.register('team',TeamViewset)
router.register('workarr',WorkArrViewset)

#Function which will check passcode then fetch data fromDB and calculate salary and then send response with employeename.