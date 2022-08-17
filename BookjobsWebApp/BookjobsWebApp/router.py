from jobappapi.viewsets import JobsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('job',JobsViewset)