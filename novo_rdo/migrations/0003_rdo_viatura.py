# Generated by Django 2.2.2 on 2019-06-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_rdo', '0002_remove_rdo_viatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdo',
            name='viatura',
            field=models.CharField(default=None, max_length=50),
        ),
    ]