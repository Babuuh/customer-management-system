# Generated by Django 3.1 on 2021-02-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210211_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
