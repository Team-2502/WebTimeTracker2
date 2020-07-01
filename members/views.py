from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import Member
from .forms import NewMemberForm


def index(request):
    context = {'members': Member.objects.filter(logged_in=False).order_by('first_name'), 'members_signed_in': Member.objects.filter(logged_in=True)}
    return render(request, 'members/index.html', context)


def member_detail(request, first_name, last_name):
    try:
        member = get_object_or_404(Member, first_name=first_name, last_name=last_name)
    except Member.DoesNotExist:
        raise Http404("Team member does not exist")
    return render(request, 'members/member_detail.html', {'member': member})


def create_member(request):
    if request.method == "POST":
        form = NewMemberForm(request.POST)
        if form.is_valid():
            new_member = Member(first_name=str.lower(request.POST['first_name']), last_name=str.lower(request.POST['last_name']))
            new_member.save()
            return HttpResponseRedirect('/members/%s/%s' % (new_member.first_name, new_member.last_name))
    else:
        form = NewMemberForm()

    return render(request, 'members/member_new.html', {'form': form})


def signed_in(request):
    return


def signed_out(request):
    return


def member_list(request):
    return render(request, 'members/members_all.html')


def members_here(request):
    return
