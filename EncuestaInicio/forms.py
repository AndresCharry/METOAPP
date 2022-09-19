from django  import forms

class FormularioEncuestaInicio(forms.Form):
    tipo_cultivo = forms.CharField(label='Tipo de cultivo', required=True,max_length= 40)
    surcos = forms.BooleanField(label='surco', required=False, initial=False)
