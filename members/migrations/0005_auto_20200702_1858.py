# Generated by Django 3.0.7 on 2020-07-02 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200702_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sign_in_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
