from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from hello.views import member_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
    path('create/',member_create_view)
]
