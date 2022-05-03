# Generated by Django 4.0.3 on 2022-04-21 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='useraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=120)),
                ('ifvoted', models.BooleanField(default=False)),
                ('voteresult', models.CharField(default='0', max_length=1)),
                ('etc', models.TextField(blank=True, null=True)),
                ('poll_case', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminapp.poll_cases')),
            ],
        ),
        migrations.CreateModel(
            name='logineduseraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=120)),
                ('related_useraccount', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]