from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Member


def index(request):
    return render(request, 'members/index.html')


def member_detail(request, first_name, last_name):
    if request.method == "POST":
        new_member = Member(first_name=str.lower(request.POST['first_name']), last_name=str.lower(request.POST['last_name']))
        new_member.save()
        return render(request, 'members/member_detail.html', {'member': new_member})
    else:
        try:
            member = get_object_or_404(Member, first_name=first_name, last_name=last_name)
        except Member.DoesNotExist:
            raise Http404("Team member does not exist")
        return render(request, 'members/member_detail.html', {'member': member})


def create_member(request):
    return render(request, 'members/member_new.html')


def signed_in(request):
    return


def signed_out(request):
    return


def member_list(request):
    return render(request, 'members/members_all.html')


def members_here(request):
    return
