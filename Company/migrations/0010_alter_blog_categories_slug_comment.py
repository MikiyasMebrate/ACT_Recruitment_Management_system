# Generated by Django 4.2.2 on 2023-07-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0009_alter_blog_description_remove_blog_type_blog_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_categories',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company.blog')),
            ],
        ),
    ]
