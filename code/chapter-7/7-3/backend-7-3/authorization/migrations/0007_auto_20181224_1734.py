# Generated by Django 2.0 on 2018-12-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20181224_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=256),
        ),
    ]
