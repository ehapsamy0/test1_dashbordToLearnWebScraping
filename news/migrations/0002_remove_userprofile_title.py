# Generated by Django 2.2.6 on 2019-10-05 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='title',
        ),
    ]
