# Generated by Django 3.1.4 on 2021-01-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TT', '0005_auto_20210113_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]