# Generated by Django 2.0.2 on 2018-03-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tech'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech',
            name='branch',
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='technology',
            field=models.ManyToManyField(to='myapp.Tech'),
        ),
    ]
