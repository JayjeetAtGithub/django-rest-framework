# Generated by Django 2.0.2 on 2018-03-07 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180307_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bucket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Bucketlist'),
        ),
    ]
