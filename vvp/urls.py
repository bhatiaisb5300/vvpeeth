from django.urls import path
from . import views
app_name = 'vvp'
urlpatterns = [
    path('',views.index,name='index'),
    path('alumni/',views.alumni,name='alumni'),
    path('our-gems/',views.our_gems_view,name='gems'),
    path('our-gems/add/',views.gems_form,name='gems_form'),
    path('gallery/',views.gallery_view,name='gallery'),
    path('gallery/add/',views.gallery_form,name='gallery_form'),
    path('notices-events/',views.notice,name='notice'),
    path('notices-events/add/',views.notice_form,name='notice_form'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('staff/',views.staffmembers,name='staff'),
    path('committee',views.committeemembers,name='committee'),
]
