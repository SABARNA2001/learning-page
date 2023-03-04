from django.contrib import admin
from django.urls import path
from learning_app import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('masterlogin/',views.masterloginloginpage,name='masterlogin'),
    path('studentlogin/',views.studentloginloginpage,name='studentlogin'),
    path('masterdashboard/',views.masterdashboardpage,name='masterdashboard'),
    path('studentdashboard/',views.studentdashboardpage,name='studentdashboard'),
    path('logout/', views.logout_view, name='logout'),
]