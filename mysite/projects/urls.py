from django.conf.urls import url
from . import views
from projects.models import Project

urlpatterns = [
    url(r'^$', views.home, name='projectslist')
]
