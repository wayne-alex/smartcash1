from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/<str:referrer>/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('package/', views.package, name='package'),
    path('buy_package/<str:username>/<str:package_type>', views.buy_package, name='buy_package'),
    path('views/', views.w_views, name='views'),
    path('bought/<str:package_type>', views.bought, name='bought'),
    path('buy/', views.package_buy, name='buy'),
    path('logout/', views.logout_user, name='logOut'),
]