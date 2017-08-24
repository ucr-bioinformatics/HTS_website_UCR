from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from  accounts.views import (login_view, register_view, logout_view)

urlpatterns = [ 
                url(r'^login/', login_view, name='login'),
            ]
