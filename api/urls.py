from django.urls import path
from api import views as api_views


urlpatterns = [
    # All services
    path('services/', api_views.ServiceListView.as_view(), name='service_list'),
    # All Projects
    path('projects/', api_views.ProjectListView.as_view(), name='project_list'),
]
