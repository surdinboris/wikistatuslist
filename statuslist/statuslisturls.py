from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='statuslist'
#url (r'^statuslist', include(admin.site.urls)),

urlpatterns = [
url(r'^main/', views.main, name='main'),
url(r'^detail/(?P<ibox>ibox[0-9]+)/', views.detail, name='detail'),
]


#url(r'^(?P<ibox>[0-9]+)/$', views.detail, name='detail'),