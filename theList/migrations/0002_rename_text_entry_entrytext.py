# Generated by Django 4.1.5 on 2023-02-04 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theList', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='text',
            new_name='entryText',
        ),
    ]