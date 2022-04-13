# Generated by Django 4.0.3 on 2022-04-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='useraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('votername', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('votesn', models.CharField(max_length=12)),
                ('ifvoted', models.BooleanField(default=False)),
                ('voteresult', models.CharField(default='0', max_length=1)),
                ('etc', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(verbose_name=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
