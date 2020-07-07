"""RTE_HMI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from site_RTE import views


urlpatterns = [
    path('home', views.home_page,name='home-page'),
    path('admin-co', views.admin_co,name='admin-co'),
    path('user-request', views.user_request,{},name='user-request'),
    path('admin-hist', views.admin_hist,name='admin-hist'),
    path('admin-input', views.admin_input,name='admin-input'),
    path('admin-main', views.admin_main,name='admin-main'),
    path('fault', views.func_fault,name='fault'),
    path('grid-dist', views.grid_dist,name='grid-dist'),
    path('interrupt', views.func_interrupt,name='interrupt'),
    path('outage', views.func_outage,name='outage'),
    path('user-fault', views.user_fault,name='user-fault'),
    path('user-grid-dist', views.user_grid_dist,name='user-grid-dist'),
    path('user-interrupt', views.user_interrupt,name='user-interrupt'),
    path('user-outage', views.user_outage,name='user-outage'),
]
(r'^login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/login/'}),
