# Generated by Django 2.0.3 on 2018-07-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_auto_20180723_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
