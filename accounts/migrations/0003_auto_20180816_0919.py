# Generated by Django 2.1 on 2018-08-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180815_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
