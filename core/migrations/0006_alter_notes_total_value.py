# Generated by Django 4.0.3 on 2022-04-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_items_note_alter_observation_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor total'),
        ),
    ]
