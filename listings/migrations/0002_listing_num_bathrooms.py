# Generated by Django 4.1.2 on 2022-10-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='num_bathrooms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
