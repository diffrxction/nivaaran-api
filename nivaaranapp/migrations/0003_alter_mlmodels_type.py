# Generated by Django 3.2.20 on 2023-07-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nivaaranapp', '0002_mlmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlmodels',
            name='type',
            field=models.CharField(choices=[('violence', 'violence'), ('detection', 'detection'), ('intrusion', 'intrusion')], max_length=30),
        ),
    ]