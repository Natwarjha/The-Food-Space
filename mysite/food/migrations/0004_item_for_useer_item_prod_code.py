# Generated by Django 4.2.7 on 2023-12-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_useer',
            field=models.CharField(default='RestOwner', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=50),
        ),
    ]
