from django.urls import path

from . import views

urlpatterns = [
	path('antixss',views.antixss, name="antixss"),
	path('xss',views.xss, name="xss"),
    path('', views.index, name='index'),
]