from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.utils import timezone

from datetime import datetime
import pytz
from decimal import Decimal
import csv

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
            return HttpResponseRedirect('/members/')
    else:
        form = NewMemberForm()

    return render(request, 'members/member_new.html', {'form': form})


def signed_in(request):
    member = Member.objects.get(id=request.POST['login_select'])
    member.logged_in = True
    member.sign_in_time = timezone.now()
    member.save()
    return render(request, 'members/signed_in.html')


def signed_out(request):
    member = Member.objects.get(id=request.POST['logout_select'])
    member.logged_in = False

    tz = pytz.timezone('America/Chicago')
    current_time = datetime.now(tz=tz)
    diff = current_time - member.sign_in_time

    member.num_hours += Decimal(diff.total_seconds() / 3600).quantize(Decimal('1.00'))
    member.save()

    return render(request, 'members/signed_out.html')


def member_list(request):
    return render(request, 'members/members_all.html', {'members': Member.objects.order_by('first_name')})


def members_here(request):
    return render(request, 'members/members_here.html', {'members': Member.objects.filter(logged_in=True).order_by('first_name')})


def create_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="member_hours.csv"'

    writer = csv.writer(response)
    for member in Member.objects.order_by('first_name'):
        writer.writerow([member.first_name, member.last_name, member.num_hours])

    return response
