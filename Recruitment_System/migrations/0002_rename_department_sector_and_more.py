# Generated by Django 4.2.3 on 2023-07-18 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Sector',
        ),
        migrations.RenameField(
            model_name='job_posting',
            old_name='department',
            new_name='Sector',
        ),
    ]