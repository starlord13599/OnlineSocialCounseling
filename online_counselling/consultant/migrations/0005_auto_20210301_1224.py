# Generated by Django 2.2.12 on 2021-03-01 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0004_remove_consultant_state'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsutancyType',
            new_name='ConsultancyType',
        ),
    ]