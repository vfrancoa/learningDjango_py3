# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('asunto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('contenido', models.TextField()),
                ('mejor_respuesta', models.BooleanField(default=False, verbose_name='Respuesta preferida')),
                ('Pregunta', models.ForeignKey(to='preguntasyrespuestas.Pregunta')),
            ],
        ),
    ]
