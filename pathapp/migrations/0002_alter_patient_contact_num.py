# Generated by Django 4.2.2 on 2023-07-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='contact_num',
            field=models.IntegerField(),
        ),
    ]
