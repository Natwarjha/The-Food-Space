# Generated by Django 4.2.7 on 2024-02-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]
