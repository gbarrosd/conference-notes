# Generated by Django 4.0.3 on 2022-04-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_notes_plate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='observation',
        ),
        migrations.AddField(
            model_name='notes',
            name='situacion',
            field=models.CharField(max_length=20, null=True, verbose_name='Situação'),
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.CharField(max_length=250, null=True, verbose_name='Observação')),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.notes')),
            ],
        ),
    ]
