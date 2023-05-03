from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def pagPrincipal(request):

    return render (request,'app/pagPrincipal.html')

def pagIniciosesion(request):

    return render (request,'app/pagIniciosesion.html')

def pagNosotros(request):

    return render (request,'app/pagNosotros.html')

def pagRegistro(request):

    return render (request,'app/pagRegistro.html')

def pagEmpleo(request):

    return render (request,'app/pagEmpleo.html')

def pagRegistroEmp(request):

    return render (request,'app/pagRegistroEmp.html')



def form_persona(request):
    datos = {
        'form': PersonaForm()
    }

    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Guardado correctamente"

    return render(request, 'app/form_persona.html',datos)

def form_personaE(request, id):
    auto = Persona.objects.get(correo_per=id)
    datos = {
        'form': PersonaForm(instance=auto)
    }
    if request.method=='POST':
        formulario= PersonaForm(data=request.POST, instance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'app/form_personaE.html', datos)


def listar_E_persona(request):
    Personas = Persona.objects.all()
    datos = {
        "personas":Personas
    }
    return render(request, 'app/listar_E_persona.html',datos)

def form_D_persona(request, id):
    aut = persona.objects.get(id=id)
    datos = {
        'form': PersonaForm(instance=aut)
    }
    if request.method=='POST':
        formulario= PersonaForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado Correctamente"

    return render(request, 'app/form_D_persona.html', datos)