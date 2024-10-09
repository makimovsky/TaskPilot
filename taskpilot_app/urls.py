from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskpilot_app import views

router = DefaultRouter()
router.register('worker', views.WorkersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

