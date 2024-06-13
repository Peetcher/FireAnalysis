from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirDivisionsViewSet, FiresDinamicsListView

router = DefaultRouter()
router.register(r'airdivisions', AirDivisionsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('fires_dinamics/', FiresDinamicsListView.as_view(), name="fires_dinamics"),
]
