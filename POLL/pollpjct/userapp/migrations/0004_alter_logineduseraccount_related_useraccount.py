# Generated by Django 4.0.3 on 2022-04-21 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0003_logineduseraccount_related_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logineduseraccount',
            name='related_useraccount',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
