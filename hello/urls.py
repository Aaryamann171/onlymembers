from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('delete_member/', views.member_delete_view, name='delete_member'),
    path('delete/<int:id>/', views.confirm_delete, name='confirm_delete'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
]
