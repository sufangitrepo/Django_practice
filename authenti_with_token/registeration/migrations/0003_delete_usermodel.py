# Generated by Django 4.1 on 2022-08-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0002_remove_usermodel_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
