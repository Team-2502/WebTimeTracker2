from django.urls import path

from . import views

urlpatterns = [
    # /members/
    path('', views.index, name='index'),
    # /members/ryan/alexander
    path('<first_name>/<last_name>/', views.member_detail, name='member_detail'),
    # /members/new_member
    path('new_member', views.create_member, name='new_member'),
    # /members/signed_in
    path('signed_in', views.signed_in, name='signed_in'),
    # /members/signed_out
    path('signed_out', views.signed_out, name='signed_out'),
    # /members/view_all
    path('view_all', views.member_list, name='view_all'),
    # /members/export
    path('export', views.create_export, name='export'),
    # /members/at_the_room
    path('at_the_room', views.members_here, name='at_the_room'),
]
