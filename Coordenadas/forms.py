from django  import forms

class FormularioCoordenadas(forms.Form):
    lat_1 = forms.FloatField(label='Latitud 1', required=True)
    log_1 = forms.FloatField(label='Longitud 1', required=True)
    h1 = forms.FloatField(label='Longitud 1', required=True)
    lat_2 = forms.FloatField(label='Latitud 2', required=True)
    log_2 = forms.FloatField(label='Longitud 2', required=True)
    h2 = forms.FloatField(label='Longitud 1', required=True)
    lat_3 = forms.FloatField(label='Latitud 3', required=True)
    log_3 = forms.FloatField(label='Longitud 3', required=True)
    h3 = forms.FloatField(label='Longitud 1', required=True)
    lat_4 = forms.FloatField(label='Latitud 4', required=True)
    log_4 = forms.FloatField(label='Longitud 4', required=True)
    h4 = forms.FloatField(label='Longitud 1', required=True)