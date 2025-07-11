from rest_framework.routers import DefaultRouter
from .views import JobRecordViewSet

router = DefaultRouter()
router.register(r'jobs', JobRecordViewSet, basename='jobrecord')

urlpatterns = router.urls