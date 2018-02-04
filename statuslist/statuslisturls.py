from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='statuslist'
#url (r'^statuslist', include(admin.site.urls)),

urlpatterns = [
url(r'^status/', views.main, name='status'),
url(r'^detail/(?P<ibox>.*)/', views.detail, name='detail'),
url(r'^jstst/', views.jstst, name='jstst'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#url(r'^(?P<ibox>[0-9]+)/$', views.detail, name='detail'),