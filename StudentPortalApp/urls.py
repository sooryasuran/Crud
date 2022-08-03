from django.urls import path

from StudentPortalApp import views,apiviews

urlpatterns = [
    path('',views.homeview,name='homeview'),
    path('loginview',views.loginview,name='loginview'),
    path('adminhome',views.adminview,name='adminhome'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentprofile',views.studentprofile,name='studentprofile'),

    path('login_view',apiviews.login_view,name='login_view')

]