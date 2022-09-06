from django  import forms

class Proyecto(forms.Form):
    nombre_proyecto = forms.CharField(label="nombre del proyecto", max_length= 100, required=True)
    nombre_campaña =  forms.CharField(label="nombre de la campaña", max_length= 100, required=True)
    dia_plantacion = forms.CharField(label="Dia de la plantacion", max_length= 100, required=True)
    fecha = forms.CharField(label="nombre del proyecto", required=True)

class campañas(forms.Form):
    nombre_campaña =  forms.CharField(label="nombre de la campaña", max_length= 100, required=True)
    dia_plantacion = forms.CharField(label="Dia de la plantacion", max_length= 100, required=True)
    fecha = forms.CharField(label="nombre del proyecto", required=True)

class Fechas(forms.Form):
    fecha = forms.CharField(label="nombre del proyecto", required=True)

class NombreProyecto(forms.Form):
    nombre_proyecto = forms.CharField(label="nombre del proyecto", max_length= 100, required=True)

class NombreCampaña(forms.Form):
    nombre_campaña = forms.CharField(label="nombre de la campaña", max_length= 100, required=True)

class Fecha(forms.Form):
    fecha = forms.CharField(label="fecha", max_length= 100, required=True)
