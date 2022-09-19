from django  import forms

class FormularioCoordenadas(forms.Form):
    tipo_cultivo = forms.CharField(label='Tipo de cultivo', required=True,max_length= 40)
    file = forms.FileField() # for creating file input
