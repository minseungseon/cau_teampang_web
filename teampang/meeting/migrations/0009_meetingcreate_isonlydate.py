# Generated by Django 3.1 on 2020-09-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0008_auto_20200831_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingcreate',
            name='isOnlyDate',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
