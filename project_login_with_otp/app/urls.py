from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    # path('signup', views.signup,name="signup"),

    path('add/',views.add,name="add"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('login_check/',views.login_check,name="login_check"),
    path('store/',views.store,name="store"),
    path('show', views.show,name="show"),
    path('edit/<int:id>/', views.edit, name='contact-edit'),
    path('update/', views.update,name="update"),
    path('delete/<int:id>/', views.delete,name="delete"),
    # path('signin/', views.signin,name="signin"),
    # path('signout', views.signout,name="signout"),
    path('showformdata', views.showformdata, name='showdata'),
    path('login_check/verification', views.verification, name='verification')
    
]
