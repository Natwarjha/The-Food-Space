# Generated by Django 4.2.7 on 2024-01-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_itempictures_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='location', max_length=100),
        ),
    ]
