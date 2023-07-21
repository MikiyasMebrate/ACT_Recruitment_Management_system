# Generated by Django 4.2.3 on 2023-07-21 05:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0004_alter_application_slug_alter_bookmarks_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarks',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sector',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
