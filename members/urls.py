from django.urls import path

from . import views

urlpatterns = [
    # /members/
    path('', views.index, name='index'),
    # /members/ryan/alexander
    path('<first_name>/<last_name>/', views.member_detail, name='member_detail'),
    # /members/new_member
    path('new_member', views.create_member, name='new_member')
]
