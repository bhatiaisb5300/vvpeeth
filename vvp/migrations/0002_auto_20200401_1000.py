# Generated by Django 2.1.7 on 2020-04-01 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='current_employment_status',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='our_gems',
            name='Class',
            field=models.CharField(choices=[('10th', '10th'), ('12th', '12th')], max_length=10),
        ),
    ]
