# Generated by Django 5.1.2 on 2024-10-25 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Name must start with a capital letter!')])),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z]', message='Name must start with a capital letter!')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z]', message='Name must start with a capital letter!')])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
