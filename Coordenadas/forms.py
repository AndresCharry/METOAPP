from django  import forms

class FormularioCoordenadas(forms.Form):
    file = forms.FileField() # for creating file input
