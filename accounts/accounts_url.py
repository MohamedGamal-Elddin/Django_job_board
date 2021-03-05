from django.urls import path
from . import views
# from django.contrib.models import view as as_view

app_name='accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/Edit/',views.edit_profile,name='edit_profile'),
]
