# Generated by Django 3.1.4 on 2021-07-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_auto_20210717_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='armyexam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
