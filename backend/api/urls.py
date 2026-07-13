from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, InterviewViewSet

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'interviews', InterviewViewSet)

urlpatterns = router.urls