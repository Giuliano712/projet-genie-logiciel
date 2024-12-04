from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'planner'

urlpatterns = [
    path('', views.Planner.as_view(), name='planner_page'),
    path('developer/', views.DeveloperHomeView.as_view(), name='developer_page'),
    path('project_manager/', views.ProjectManagerHomeView.as_view(), name='project_manager_page'),
    path('developer/clientcompany/<uuid:pk>/', views.ClientCompanyDetailView.as_view(), name='client_company_detail'),
]

# <uuid:id> uses the id of the clientcompany