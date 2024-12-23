from django.urls import path
from .import views

urlpatterns = [

    path('RegisterUser/',views.RegisterUser,name='RegisterUser'),
    path('RegisterVendor/',views.RegisterVendor,name='RegisterVendor'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('myAccount/',views.myAccount,name='myAccount'),
    path('customerDashboard/',views.customerDashboard,name='customerDashboard'),
    path('venderDashboard/',views.vendorDashboard,name='venderDashboard'),
]
