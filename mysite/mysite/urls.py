from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^proj/', include('proj.urls')),
    url(r'^admin/', admin.site.urls),
]