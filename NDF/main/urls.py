from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^stud_profile/$', views.stud_profile, name='stud_profile'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^stud_full_dept/$', views.stud_full_dept, name='stud_full_dept'),
    url(r'^stud_full_lab/$', views.stud_full_lab, name='stud_full_lab'),
    url(r'^faculty_profile/$', views.faculty_profile, name='faculty_profile'),
    url(r'^library_profile/$', views.library_profile, name='library_profile'),
    url(r'^caretaker_profile/$', views.caretaker_profile, name='caretaker_profile'),
    url(r'^gymkhana_profile/$', views.gymkhana_profile, name='gymkhana_profile'),
    url(r'^assireg_profile/$', views.assireg_profile, name='assireg_profile'),
    url(r'^warden_profile/$', views.warden_profile, name='warden_profile'),
    url(r'^onlinecc_profile/$', views.onlinecc_profile, name='onlinecc_profile'),
    url(r'^cc_profile/$', views.cc_profile, name='cc_profile'),
    url(r'^thesis_manager_profile/$', views.thesis_manager_profile, name='thesis_manager_profile'),
    url(r'^lab_profile/$', views.lab_profile, name='lab_profile'),
    url(r'^hod_profile/$', views.hod_profile, name='hod_profile'),
    url(r'^account_profile/$', views.account_profile, name='account_profile'),


]

    #url(r'stud_profile/1$', views.stud_profile, names='stud_profile'),
    #url(r'^stud_profile/(?P<username>\w+)/', views.stud_profile, name='stud_overall'),
    #url(r'^stud_profile/(.*)/dept$', views.stud_full_dept, name='stud_dept'),
    #url(r'^stud_profile/(.*)/lab$',views.stud_full_lab , name='stud_lab'),


#index is view name