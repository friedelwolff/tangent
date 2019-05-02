from django.urls import path
from employees import views


urlpatterns = [
        path('', views.IndexView.as_view()),
]
