from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta


# Create your views here.

def index(request):
	preguntas = Pregunta.objects.all()
	#respuesta_string = "Preguntas <br />"
	#respuesta_string += '<br/>'.join([ "id: %s, asunto: %s" % (p.id, p.asunto) for p in preguntas ])
	#return HttpResponse(respuesta_string)
	return render_to_response('preguntasyrespuestas/index.html', 
									{'preguntas':preguntas})

"""
def pregunta_detalle(request, pregunta_id):
	try:
		pregunta = Pregunta.objects.get(pk=pregunta_id)
	except Pregunta.DoesNotExist:
		raise Http404
	return HttpResponse("%s?" % pregunta.asunto)
"""
def pregunta_detalle(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	#return HttpResponse("%s?" % pregunta.asunto)
	return render_to_response('preguntasyrespuestas/pregunta_detalle.html', 
									{'pregunta': pregunta})
