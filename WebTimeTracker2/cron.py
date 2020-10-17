from members.models import Member, Appearance
from decimal import Decimal
from datetime import datetime


def sign_all_out():
    print("Signing everyone out")
    members = Member.objects.all().filter(logged_in=True)
    for member in members:
        member.logged_in = False
        diff = datetime.now() - member.sign_in_time
        added_hours = Decimal(diff.total_seconds() / 3600).quantize(Decimal('1.00'))
        member.num_hours += added_hours
        member.num_hours_virtual += added_hours
        member.save()

        appearance = Appearance(date=member.sign_in_time.date(), length=added_hours,
                                start_time=member.sign_in_time.time(),
                                end_time=datetime.now().time(), member=member, activity='FORGOT TO SIGN OUT',
                                location='virtual')
        appearance.save()
