# Generated by Django 3.2 on 2021-06-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0004_auto_20210611_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='rede',
            name='monitorado',
            field=models.BooleanField(default=False, verbose_name='Monitorar no nagios'),
        ),
    ]