from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^new/$', views.create_course, name='create_course'),
    url(r'(?P<course>[a-zA-z]+)/$', views.course_details, name='course_detals'),
]