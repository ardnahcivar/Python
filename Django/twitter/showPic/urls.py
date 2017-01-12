from django.conf.urls import url
from . import views

app_name = 'showPic'

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^getUserData/$', views.getUserData, name='userData')
]
