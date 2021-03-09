from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeMessageView.as_view(), name="welcome"),
    path('questions/', views.QuestionListView.as_view(), name="questions"),
]