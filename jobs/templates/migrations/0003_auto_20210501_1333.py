# Generated by Django 3.1.2 on 2021-05-01 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210501_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cost',
            old_name='cost',
            new_name='costModel',
        ),
        migrations.RenameField(
            model_name='cost',
            old_name='date',
            new_name='dateModel',
        ),
    ]