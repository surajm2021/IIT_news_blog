# Generated by Django 3.1.4 on 2020-12-15 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_blog',
            name='image',
        ),
    ]