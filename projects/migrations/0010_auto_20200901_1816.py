# Generated by Django 3.0.8 on 2020-09-01 10:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_auto_20200901_1758'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together={('owner', 'project')},
        ),
    ]
