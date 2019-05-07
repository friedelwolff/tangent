from django.urls import path
from employees import views


urlpatterns = [
        path('', views.IndexView.as_view()),
        path('list/', views.EmployeesListView.as_view(), name='list'),
        path('statistics/', views.EmployeeStatsView.as_view(), name='stats'),
        path('search/', views.SearchView.as_view(), name='search'),
        path('myprofile/', views.MyProfileView.as_view(), name='myprofile'),
]
