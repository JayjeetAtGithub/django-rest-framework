# Generated by Django 2.0.2 on 2018-03-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bucket_id',
            field=models.IntegerField(),
        ),
    ]
