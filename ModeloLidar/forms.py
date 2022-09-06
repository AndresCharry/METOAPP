from platform import platform
from unittest.util import _MAX_LENGTH
from django  import forms

numero_variables = (
                        ("1","1"),
                        ("2","2"),
                        ("3","3"),
                        ("4","4"),
                        ("5","5"),
                        ("6","6"),
                        ("7","7"),
                        ("8","8")
                    )

numero_velocidad = (
                        ("25","25"),
                        ("26","26"),
                        ("27","27"),
                        ("28","28"),
                        ("29","29"),
                        ("30","30"),
                        ("31","31"),
                        ("32","32"),
                        ("33","33"),
                        ("34","34"),
                        ("35","35"),
                        ("36","36"),
                        ("37","37"),
                        ("38","38"),
                        ("39","39"),
                        ("40","40"),
                        ("41","41"),
                        ("42","42"),
                        ("43","43"),
                        ("44","44"),
                        ("45","45"),
                        ("46","46"),
                        ("47","47"),
                        ("48","48"),
                        ("49","49"),
                        ("50","50")
                    )
class FormularioModelo(forms.Form):
    tZ = forms.FloatField(label='Altura del LIDAR', required=True)
    alpha = forms.FloatField(label='Angulo del LIDAR', required=True)
    platform_speed = forms.ChoiceField(choices = numero_velocidad)
    angular_ring_resolution = forms.FloatField(label='Resolucion angular del anillo', required=True)
    numero_anillos = forms.ChoiceField(choices = numero_variables)

class FormularioModelo2(forms.Form):
    anillo1 =  forms.FloatField(label=' anillo1 ', required=False)
    anillo2 =  forms.FloatField(label=' anillo2 ', required=False)
    anillo3 =  forms.FloatField(label=' anillo3 ', required=False)
    anillo4 =  forms.FloatField(label=' anillo4 ', required=False)
    anillo5 =  forms.FloatField(label=' anillo5 ', required=False)
    anillo6 =  forms.FloatField(label=' anillo6 ', required=False)
    anillo7 =  forms.FloatField(label=' anillo7 ', required=False)
    anillo8 =  forms.FloatField(label=' anillo8 ', required=False)
