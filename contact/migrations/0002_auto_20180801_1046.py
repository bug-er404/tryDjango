# Generated by Django 2.0.7 on 2018-08-01 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Contact',
            new_name='contact',
        ),
    ]