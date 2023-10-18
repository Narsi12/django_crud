from django.urls import path
from .views import info,create,get_users,update_user,delete_user

urlpatterns = [
    path('info', info,name="info"),
    path('create', create,name="create"),
    path('get_users', get_users,name="get_users"),
    path('update_user/<int:pk>', update_user,name="update_user"),
    path('delete_user/<int:pk>', delete_user,name="delete_user"),

]
