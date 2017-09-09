from django.conf.urls import url

from . import views  # import views so we can use the in urls

urlpatterns = [
    url(r'^$', views.listing)
]