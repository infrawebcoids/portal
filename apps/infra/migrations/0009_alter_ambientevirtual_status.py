# Generated by Django 3.2 on 2024-11-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0008_ambientevirtual_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientevirtual',
            name='status',
            field=models.CharField(choices=[('ON', 'Ativo'), ('OFF', 'Inativo')], default='ON', max_length=3, verbose_name='status'),
        ),
    ]