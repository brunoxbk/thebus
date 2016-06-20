"""
    thebus URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'auth/', views.auth, name='auth'),
    url(r'bus_line/', views.bus_by_line, name='bus_by_line'),
    url(r'all_bus/', views.all_bus, name='all_bus'),
    url(r'all_stop/', views.bus_stop, name='bus_stop'),
    url(r'stop_line/', views.stop_by_line, name='stop_by_line'),
    url(r'lines/', views.lines, name='lines'),
    url(r'autocomplete/', views.autocomplete, name='autocomplete'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
