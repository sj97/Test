"""because URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from education import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login_success/$', core_views.login_success, name='login_success'),
   # url(r'^accounts/profile/(?P<id>\d+)', core_views.edu_new, name='edu_new'),
    url(r'^login_success/education/$', core_views.edu_new, name='edu_new'),
   #  url(r'^login/education/', core_views.edu_editable, name='edu_editable'),
   #   url(r'^login/education/(?P<name>.+)/$', core_views.edu_editable, name='edu_editable'),
    url(r'^login_success/education/(?P<id>.+)/$', core_views.edu_new, name='edu_new'),
    url(r'^login_success/company/(?P<id>.+)/$', core_views.company_new, name='company_new'),
    url(r'^login_success/company/$', core_views.company_new, name='company_new'),
    url(r'^signup/login/education/(?P<id>.+)/$', core_views.edu_new, name='edu_new'),
    url(r'^signup/login/education/$', core_views.edu_new, name='edu_new'),
    url(r'^company/$', core_views.company_new, name='company_new'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^search/$', core_views.results, name='results'),
    # url(r'^profile/(?P<id>[0-9]+)/$', core_views.non_edit, name='non_edit'),
    url(r'^login_success/education/non_edit/(?P<id>.+)/$', core_views.non_edit, name='non_edit'),
    url(r'^login_success/education/unedit/$', core_views.non_edit, name='non_edit'),
    url(r'^unedit/(?P<id>.+)/$', core_views.non_edit, name='non_edit'),
    url(r'^company_no_edit/(?P<id>[0-9]+)/$', core_views.company_no_edit, name='company_no_edit'),

    # url(r'^profile/emailsent/(?P<id>.+)/$', core_views.emailSection, name= 'emailSection'),

]


