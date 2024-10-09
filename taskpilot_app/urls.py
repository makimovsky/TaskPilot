from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskpilot_app import views

router = DefaultRouter()
# router.register('workers', views.WorkersViewSet)
# router.register('projects', views.ProjectsViewSet)
# router.register('clients', views.ClientsViewSet)
router.register('tasks', views.TasksViewSet)
router.register('comments', views.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('main/', views.main, name='main'),
    path('projects/', views.project_list, name='project_list'),
    path('workers/', views.worker_list, name='worker_list'),
    path('clients/', views.client_list, name='client_list')
]

