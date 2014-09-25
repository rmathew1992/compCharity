from django.conf.urls import patterns, url

from goodbets import views
print "Testing"
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)