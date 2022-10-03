from django  import forms
class TipoProyecto(forms.Form):
    medicion = forms.BooleanField(required=False, initial=False)
    dron = forms.BooleanField(required=False, initial=False)
    lidar = forms.BooleanField(required=False, initial=False)

class Proyecto(forms.Form):
    nombre_proyecto = forms.CharField(label="nombre del proyecto", max_length= 100, required=True)
    nombre_campaña =  forms.CharField(label="nombre de la campaña", max_length= 100, required=True)
    dia_plantacion = forms.CharField(label="Dia de la plantacion", max_length= 100, required=True)
    fecha = forms.CharField(label="nombre del proyecto", required=True)
    zona = forms.IntegerField(label="# de zonas", required=True, min_value=0)

class campañas(forms.Form):
    nombre_campaña =  forms.CharField(label="nombre de la campaña", max_length= 100, required=True)
    dia_plantacion = forms.CharField(label="Dia de la plantacion", max_length= 100, required=True)
    fecha = forms.CharField(label="nombre del proyecto", required=True)
    zona = forms.IntegerField(label="# de zonas", required=True, min_value=0)

class Fechas(forms.Form): 
    fecha = forms.CharField(label="nombre del proyecto", required=True)
    zona = forms.IntegerField(label="# de zonas", required=True, min_value=0)

class NombreProyecto(forms.Form):
    nombre_proyecto = forms.CharField(label="nombre del proyecto", max_length= 100, required=True)

class NombreCampaña(forms.Form):
    nombre_campaña = forms.CharField(label="nombre de la campaña", max_length= 100, required=True)

class Fecha(forms.Form):
    fecha = forms.CharField(label="fecha", max_length= 100, required=True)
