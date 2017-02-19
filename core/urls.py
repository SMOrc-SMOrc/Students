from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.student_list, name='main'),
    url(r'^(?P<pk>[0-9]+)/$', views.student_detail, name='detail'),

]