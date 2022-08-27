from django.urls import path
from . import views

urlpatterns = [
    path('account/signup', views.SignUpView.as_view(), name= 'signup'),
]


