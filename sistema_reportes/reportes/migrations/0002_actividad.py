# Generated by Django 5.1.6 on 2025-02-14 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='reportes.medida')),
                ('organismo_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.organismosectorial')),
            ],
        ),
    ]
