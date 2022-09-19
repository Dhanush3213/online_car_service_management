from django.urls import path
from . import views
urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('index2/',views.index2,name='index2'),
    path('viewservice',views.viewservice,name='viewservice'),
    path('viewservice2',views.viewservice2,name='viewservice2'),
    path('vieworders',views.vieworders,name='vieworders'),
    path('cancelorder/<int:id>',views.cancelorder,name='cancelorder'),
    path('profile/',views.profile,name='profile' ),
    path('editprofile/',views.editprofile,name='editprofile' ),
    path('payment/<int:id>',views.payment,name='payment'),


]