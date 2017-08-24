from django.conf.urls import url, include
from django.contrib import admin
from  accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
            ]
