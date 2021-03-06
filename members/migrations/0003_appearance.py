# Generated by Django 3.0.7 on 2020-07-06 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_team_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]
