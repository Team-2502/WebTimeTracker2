from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib import messages

from datetime import datetime
from decimal import Decimal
import csv
from string import capwords

from .models import Member, Appearance
from .forms import NewMemberForm
from django.db.models import Q


def index(request):
    context = {'members': Member.objects.filter(logged_in=False).order_by('first_name'),
               'members_signed_in': Member.objects.filter(logged_in=True)}
    return render(request, 'members/index.html', context)


def member_tracing(request, first_name, last_name, date, start_time, end_time):
    member = get_object_or_404(Member, first_name=first_name, last_name=last_name)
    appearance = get_object_or_404(Appearance, date=date, start_time=start_time, end_time=end_time, member=member)
    appearances1 = Appearance.objects.all().filter(date=date, location='in_person')
    appearances2 = appearances1.exclude(Q(end_time__lt=start_time) | Q(start_time__gt=end_time))
    appearances = list(appearances2.exclude(member=member))
    return render(request, 'members/member_tracing.html', {'member': member, 'appearance': appearance, 'appearances': appearances})


def member_detail(request, first_name, last_name):
    try:
        member = get_object_or_404(Member, first_name=first_name, last_name=last_name)
        rank = list(Member.objects.all().order_by('-num_hours')).index(member) + 1
    except Member.DoesNotExist:
        raise Http404("Team member does not exist")
    return render(request, 'members/member_detail.html', {'member': member, 'rank': rank})


def create_member(request):
    if request.method == "POST":
        form = NewMemberForm(request.POST)
        if form.is_valid():
            new_member = Member(first_name=str.capitalize(request.POST['first_name']),
                                last_name=str.capitalize(request.POST['last_name']),
                                team_role=capwords((request.POST['team_role'])))
            new_member.save()
            return HttpResponseRedirect('/')
    else:
        form = NewMemberForm()

    return render(request, 'members/member_new.html', {'form': form})


def signed_in(request):
    member = Member.objects.get(id=request.POST['login_select'])
    member.logged_in = True
    member.sign_in_time = datetime.now()
    member.save()

    messages.success(request, "%s is now signed in" % member)
    messages.success(request, "The time is %s" % datetime.now().strftime(" %I:%M %p").replace(' 0', ''))
    return HttpResponseRedirect('/')


def signed_out(request):
    print(request.POST)
    member = Member.objects.get(id=request.POST['logout_select'])
    member.logged_in = False

    diff = datetime.now() - member.sign_in_time
    added_hours = Decimal(diff.total_seconds() / 3600).quantize(Decimal('1.00'))
    member.num_hours += added_hours
    if request.POST['location'] == 'virtual':
        member.num_hours_virtual += added_hours
    elif request.POST['location'] == 'in_person':
        member.num_hours_in_person += added_hours
    member.save()

    appearance = Appearance(date=member.sign_in_time.date(), length=added_hours, start_time=member.sign_in_time.time(),
                            end_time=datetime.now().time(), member=member, activity=request.POST['activity'],
                            location=request.POST['location'])
    appearance.save()

    messages.success(request, "%s is now signed out" % member)
    messages.success(request, "Signed in for %.2f hours" % added_hours)
    return HttpResponseRedirect('/')


def member_list(request):
    return render(request, 'members/members_all.html', {'members': Member.objects.order_by('-num_hours')})


def members_here(request):
    return render(request, 'members/members_here.html',
                  {'members': Member.objects.filter(logged_in=True).order_by('first_name')})


def create_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="member_hours.csv"'

    writer = csv.writer(response)
    writer.writerow(['First', 'Last', 'Total', 'Virtual', 'In Person'])
    for member in Member.objects.order_by('first_name'):
        writer.writerow([member.first_name, member.last_name, member.num_hours, member.num_hours_virtual,
                         member.num_hours_in_person])

    return response
