# Generated by Django 3.1 on 2021-02-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210216_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to=''),
        ),
    ]
