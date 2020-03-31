from django.urls import path
from . import views
app_name = 'vvp'
urlpatterns = [
    path('',views.index,name='index'),
    path('alumni/',views.alumni,name='alumni'),
    path('our-gems/',views.our_gems,name='gems'),
    path('gallery/',views.gallery,name='gallery'),
    path('notices-events/',views.notice,name='notice'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('staff/',views.staffmembers,name='staff'),
    path('committee',views.committeemembers,name='committee'),
]
