# Generated by Django 2.1.7 on 2020-04-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvp', '0004_auto_20200404_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='s_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='staff',
            name='s_no',
            field=models.IntegerField(default=0),
        ),
    ]
