# Generated by Django 3.2 on 2024-12-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_servidortenants_tenants'),
        ('infra', '0011_alter_ambientevirtual_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='tenants',
            field=models.ManyToManyField(blank=True, to='core.Tenants'),
        ),
    ]
