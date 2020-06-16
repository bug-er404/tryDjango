# Generated by Django 2.0.7 on 2018-08-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=15)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
