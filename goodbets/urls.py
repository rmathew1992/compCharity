from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from goodbets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^challenge/', views.challenge, name='challenge'),
    url(r'^home/', views.home, name='home'),
    url(r'^material/', views.material, name='material-design'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
