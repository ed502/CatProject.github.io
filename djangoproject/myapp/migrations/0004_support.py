# Generated by Django 2.2.3 on 2019-08-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('supporter', models.CharField(max_length=20)),
                ('money', models.IntegerField(default=0)),
                ('status', models.BooleanField(default='false')),
            ],
        ),
    ]
