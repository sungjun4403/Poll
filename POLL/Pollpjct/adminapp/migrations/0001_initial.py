# Generated by Django 4.0.3 on 2022-04-21 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll_Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_case_num', models.CharField(max_length=3)),
                ('poll_name', models.CharField(blank=True, default='-1', max_length=100, null=True)),
                ('poll_status', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CandidateNum', models.CharField(max_length=3)),
                ('side', models.CharField(max_length=50)),
                ('CandidateName', models.CharField(max_length=20)),
                ('votes', models.IntegerField(blank=True, default=0, null=True)),
                ('Poll_Case_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminapp.poll_cases')),
            ],
        ),
    ]