from django.urls import path
from .views import pagPrincipal,pagIniciosesion,pagEmpleo,pagNosotros,pagRegistro,pagRegistroEmp,form_persona,form_personaE

urlpatterns = [
    path('pag-principal', pagPrincipal, name="pagPrincipal"),
    path('pag-Iniciosesion/', pagIniciosesion, name='pagIniciosesion'),
    path('pag-nosotros/', pagNosotros, name='pagNosotros'),
    path('pag-registro/', pagRegistro, name="pagRegistro"),
    path('pag-empleo/', pagEmpleo, name="pagEmpleo"),
    path('pag-registroEmp/', pagRegistroEmp, name="pagRegistroEmp"),
    path('form-persona',form_persona , name="form_persona"),
    path('form-personaEdit',form_personaE , name="form_personaE"),
]
