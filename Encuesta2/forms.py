from django  import forms


numero_variables = (
                        ("1","1"),
                        ("2","2"),
                        ("3","3"),
                        ("4","4"),
                        ("5","5"),
                        ("6","6"),
                        ("7","7"),
                        ("8","8"),
                        ("9","9"),
                        ("10","10"),
                        ("11","11"),
                        ("12","12"),
                        ("13","13"),
                        ("14","14"),
                        ("15","15"),
                        ("16","16"),
                        ("17","17"),
                        ("18","18"),
                        ("19","19"),
                        ("20","20")
                    )
numero_marcadores = (
                        ("0","0"),
                        ("4","4"),
                        ("5","5"),
                        ("6","6"),
                        ("7","7"),
                        ("8","8"),
                        ("9","9"),
                        ("10","10"),
                        ("11","11"),
                        ("12","12"),
                        ("13","13"),
                        ("14","14"),
                        ("15","15"),
                        ("16","16"),
                        ("17","17"),
                        ("18","18"),
                        ("19","19"),
                        ("20","20"),
                        ("21","21"),
                        ("22","22"),
                        ("22","22"),
                        ("24","24"),
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
                    
class SCSurcos(forms.Form):
    numero_de_marcadores = forms.ChoiceField(choices = numero_marcadores)
    n_variables = forms.ChoiceField(choices = numero_variables)
    vs = forms.FloatField(label='Distancia de surco', required= False)
    n_s = forms.FloatField(label='Numero de surcos', required= False)
    v = forms.FloatField(label='Ancho de la hilera', required= False)
    num_arb = forms.FloatField(label='Numero de arboles por hilera', required= False)
    esp_arb = forms.FloatField(label='Distancia entre arboles por hilera', required= False)
    