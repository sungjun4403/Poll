# Generated by Django 4.0.3 on 2022-04-21 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_poll_cases_poll_name'),
        ('userapp', '0002_remove_useraccount_poll_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='poll_case',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminapp.poll_cases'),
        ),
    ]
