from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='statuslist'
#url (r'^statuslist', include(admin.site.urls)),

urlpatterns = [
    url(r'^home/', views.home, name='home'),
]