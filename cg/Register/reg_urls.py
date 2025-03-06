from django.urls import path
from Register import views

urlpatterns = [
    path('register/', views.reg),
]
