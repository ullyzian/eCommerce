# Generated by Django 2.2.8 on 2020-02-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200201_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
