# Generated by Django 3.1.13 on 2021-07-15 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210715_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='compose',
            new_name='composer',
        ),
    ]
