from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.rules),
    url(r'^json/', include([
        url(r'^section/$', views.json_section)
    ])),
]