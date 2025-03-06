from django.urls import path
from Login import views

urlpatterns = [
    path('',views.log,name='login'),

]
