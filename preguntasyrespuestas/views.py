from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta
from django.template import RequestContext
from preguntasyrespuestas.form import PreguntaForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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


# def pregunta_crear(request):
# 	form = PreguntaForm()
# 	return render_to_response('preguntasyrespuestas/pregunta_crear.html',
# 			{'form':form},
# 			context_instance=RequestContext(request))

@login_required
def pregunta_crear(request):
	if request.method == 'POST':
		form = PreguntaForm(request.POST)
		if form.is_valid():
			form.save()
			# pregunta = Pregunta(asunto=form.cleaned_data['asunto'],
			# 	descripcion=form.cleaned_data['descripcion'],
			# 	fecha_publicacion=timezone.now())
			# pregunta.save()
			return redirect('preguntas')
	else:
		form = PreguntaForm()
	return render_to_response('preguntasyrespuestas/pregunta_crear.html',
		{'form':form},
		context_instance=RequestContext(request))

@login_required
def pregunta_editar(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	if request.method == 'POST':
		form = PreguntaForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect('preguntas')
	else:
		form = PreguntaForm(instance=pregunta)
	return render_to_response('preguntasyrespuestas/pregunta_editar.html',
		{'form':form},
		context_instance=RequestContext(request))
