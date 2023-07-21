# Generated by Django 4.2.3 on 2023-07-20 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=40)),
                ('phone1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address', models.CharField(max_length=100)),
                ('linked_in', models.URLField(blank=True, null=True)),
                ('git_hub', models.URLField(blank=True, null=True)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Candidate/photo')),
                ('resume', models.FileField(blank=True, null=True, upload_to='Candidate/Resume')),
                ('about', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.candidate')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', froala_editor.fields.FroalaField()),
                ('vacancies', models.IntegerField()),
                ('experience', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('salary_range_start', models.FloatField()),
                ('salary_range_final', models.FloatField()),
                ('type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('freelance', 'Freelance'), ('internship', 'Internship'), ('seasonal ', 'seasonal'), ('contract', 'Contract'), ('remote', 'Remote')], max_length=30)),
                ('job_status', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateField()),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.sector')),
                ('skills', models.ManyToManyField(to='Recruitment_System.skill')),
            ],
            options={
                'ordering': ['-date_posted', '-date_closed'],
            },
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_schedule', models.DateField()),
                ('time_schedule', models.TimeField()),
                ('status', models.CharField(choices=[('scheduled', 'scheduled'), ('completed', 'completed'), ('canceled', 'canceled')], max_length=15)),
                ('job_status', models.CharField(choices=[('rejected', 'Rejected'), ('hired', 'hired')], max_length=25)),
                ('type', models.CharField(choices=[('phone', 'phone'), ('in-person', 'in-person'), ('video', 'video')], max_length=15)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.candidate')),
                ('interviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.job_posting')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40)),
                ('work_time_line_start', models.DateField()),
                ('work_time_line_end', models.DateField()),
                ('job_title', models.CharField(max_length=50)),
                ('reference_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('reference_name', models.CharField(max_length=40)),
                ('reference_email', models.CharField(max_length=40)),
                ('reference_job_title', models.CharField(max_length=40)),
                ('responsibility', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
                ('education_status', models.CharField(choices=[('highschool', 'High School'), ('Certificate', 'Certificate'), ('diploma', 'Diploma'), ('bachelor-degree', "Bachelor's degree"), ('Master-degree', "Master's Degree"), ('doctorate', 'Doctorate'), ('other', 'Other')], max_length=40)),
                ('field_of_study', models.CharField(max_length=40)),
                ('education_period_start', models.DateField()),
                ('education_period_end', models.DateField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='skill',
            field=models.ManyToManyField(to='Recruitment_System.skill'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruitment_System.job_posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('in_review', 'in review'), ('rejected', 'rejected'), ('hired', 'hired')], default='new', max_length=15)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.job_posting')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
