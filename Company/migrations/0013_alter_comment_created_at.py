# Generated by Django 4.2.2 on 2023-07-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0012_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
