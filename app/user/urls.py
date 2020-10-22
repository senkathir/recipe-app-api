from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),#name s used
    #in reverse of test
    path('token/', views.CreateTokenView.as_view(), name='token'), 
]
