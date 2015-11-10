from django.contrib import admin
from preguntasyrespuestas.models import Pregunta, Respuesta

class RespuestaInline(admin.StackedInline):
	model = Respuesta
	extra = 3


class PreguntaAdmin(admin.ModelAdmin):
	inlines = [RespuestaInline]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
