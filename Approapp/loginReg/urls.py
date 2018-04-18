from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout



urlpatterns = [
    url(r'^$', views.home),
    url('^login/$', login, {'template_name': 'loginReg/login.html'}),
    url('^logout/$', logout, {'template_name': 'loginReg/logout.html'}),
    url('^register',views.register,name='register'),
    url('^profile/', views.profile_view, name='profile_view'),
    url('^profile/edit/$', views.profile_edit, name='profile_edit'),
        ]
