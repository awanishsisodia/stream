# Generated by Django 3.1.1 on 2021-01-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodata',
            name='thimnail',
            field=models.ImageField(blank=True, upload_to='Thumnail'),
        ),
    ]