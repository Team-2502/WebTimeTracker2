from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.index, name='index'),
    # /ryan/alexander/
    path('<first_name>/<last_name>/', views.member_detail, name='member_detail'),
    # /Sarthak/Agrawal/2020-10-03/22:38:01.743136/22:51:01.922644/
    path('<first_name>/<last_name>/<date>/<start_time>/<end_time>/', views.member_tracing, name='member_tracing'),
    # /new_member/
    path('new_member', views.create_member, name='new_member'),
    # /signed_in/
    path('signed_in', views.signed_in, name='signed_in'),
    # /signed_out/
    path('signed_out', views.signed_out, name='signed_out'),
    # /view_all/
    path('view_all', views.member_list, name='view_all'),
    # /export/
    path('export', views.create_export, name='export'),
    # /at_the_room/
    path('at_the_room', views.members_here, name='at_the_room'),
]
