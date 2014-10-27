from django.conf.urls import patterns, url
from goodbets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^challenge/', views.challenge, name='challenge'),
    url(r'^home/', views.home, name='home'),
)
