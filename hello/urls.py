from django.urls import path
from .views import MemberCreateView, MemberDetailView, MemberUpdateView, home_view, member_delete_view, member_update_view, confirm_delete, register, logout_request, login_request

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', MemberCreateView.as_view(), name='member_create'),
    path('details/<pk>/', MemberDetailView.as_view(), name='member_details'),
    path('update/<pk>/', MemberUpdateView.as_view(), name='member_update'),
    path('delete_member/', member_delete_view, name='delete_member_view'),
    path('update_member/', member_update_view, name='update_member_view'),
    path('delete/<int:id>/', confirm_delete, name='confirm_delete'),
    path('register/', register, name='register'),
    path('logout/', logout_request, name='logout'),
    path('login/', login_request, name='login'),
]
