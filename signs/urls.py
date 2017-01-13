from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ScreensAll),
    url(r'^(?P<screenslug>.*)/$', views.SpecificScreen),
]
