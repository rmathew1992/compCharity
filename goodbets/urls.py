
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from goodbets import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^challenge/', views.challenge, name='challenge'),
    # url(r'^home/', views.home, name='home'),
    # url(r'^about/', views.about, name='about'),
    url(r'^login/', views.login, name='login'),
    url(r'^material/', views.material, name='material-design'),
    url(r'^feed/', views.feed, name='feed'),
    url(r'^paypal/', views.paypal_test, name='paypal'),
    url(r'^mybets/', views.mybets, name='=mybets'),
)

urlpatterns += staticfiles_urlpatterns()
