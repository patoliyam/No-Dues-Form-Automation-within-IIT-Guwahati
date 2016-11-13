from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    #url(r'stud_profile/1$', views.stud_profile, names='stud_profile'),
    #url(r'^stud_profile/(?P<username>\w+)/', views.stud_profile, name='stud_overall'),
    #url(r'^stud_profile/(.*)/dept$', views.stud_full_dept, name='stud_dept'),
    #url(r'^stud_profile/(.*)/lab$',views.stud_full_lab , name='stud_lab'),

]
#index is view name