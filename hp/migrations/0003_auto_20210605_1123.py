# Generated by Django 2.2 on 2021-06-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0002_auto_20210604_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch_100m',
            name='HFX',
            field=models.CharField(default='', max_length=20),
        ),
    ]