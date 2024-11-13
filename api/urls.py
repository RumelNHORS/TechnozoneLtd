from django.urls import path
from api import views as api_views


urlpatterns = [
    # Define API endpoints here
    path('services/', api_views.ServiceListView.as_view(), name='service_list')
]
