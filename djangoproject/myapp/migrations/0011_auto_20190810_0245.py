# Generated by Django 2.2.3 on 2019-08-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_support_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='support',
            old_name='type',
            new_name='typ',
        ),
    ]
