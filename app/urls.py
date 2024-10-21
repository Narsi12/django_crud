from django.urls import path
from .views import infouser,create,get_users,update_user,delete_user

urlpatterns = [
    path('infouser', infouser,name="info"),
    path('create', create,name="create"),
    path('get_users', get_users,name="get_users"),
    path('update_user/<int:pk>', update_user,name="update_user"),
    path('delete_user/<int:pk>', delete_user,name="delete_user"),

]
