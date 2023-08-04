from django.contrib import admin
from django.urls import path
from finalproapp1 import views

app_name='finalproapp1'

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form', views.formView,name='formView'),
    path('page', views.page,name='page'),
    path('save', views.saveData,name='saveData'),

]
