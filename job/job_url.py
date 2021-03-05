from django.urls import path
from . import views

app_name='job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('job_post/',views.job_post,name='job_post'),
    path('<str:slug>/',views.job_details,name='job_details'),

]
