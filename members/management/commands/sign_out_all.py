from django.core.management.base import BaseCommand
from members.models import Member, Appearance

from decimal import Decimal
from datetime import datetime


class Command(BaseCommand):
    help = 'Signs out all users currently signed in'

    def handle(self, *args, **options):
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
                                    end_time=datetime.now().time(), member=member, activity='Forgot to sign out',
                                    location='virtual')
            appearance.save()
        return
