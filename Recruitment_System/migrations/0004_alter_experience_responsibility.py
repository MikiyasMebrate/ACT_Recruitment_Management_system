# Generated by Django 4.2.3 on 2023-07-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0003_alter_experience_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='responsibility',
            field=models.TextField(blank=True, null=True),
        ),
    ]
