# Generated by Django 4.0.3 on 2022-04-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_poll_cases_takeendpic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll_cases',
            old_name='takeendpic',
            new_name='take_endpic',
        ),
    ]
