# Generated by Django 4.2.2 on 2023-06-23 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0007_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]