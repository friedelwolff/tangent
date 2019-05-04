from django.urls import path
from employees import views


urlpatterns = [
        path('', views.IndexView.as_view()),
        path('list/', views.EmployeesListView.as_view(), name='list'),
]
