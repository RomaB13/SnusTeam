# Generated by Django 3.2 on 2021-05-09 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_merge_0006_auto_20210509_1830_0006_auto_20210509_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
    ]
