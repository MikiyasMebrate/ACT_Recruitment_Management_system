# Generated by Django 4.2.2 on 2023-07-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_Management_System', '0006_alter_skill_options_alter_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='git_hub',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='linked_in',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job_posting',
            name='skills',
            field=models.ManyToManyField(to='Recruitment_Management_System.skill'),
        ),
        migrations.DeleteModel(
            name='Social_media',
        ),
    ]
