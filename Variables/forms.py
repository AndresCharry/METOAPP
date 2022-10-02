from django  import forms

from Variables.baseDeDatos import numero_v

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
                    )
numero_puntos = (
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
                        ("50","50"),
                        ("51","51"),
                        ("52","52"),
                        ("53","53"),
                        ("54","54"),
                        ("55","55"),
                        ("56","56"),
                        ("57","57"),
                        ("58","58"),
                        ("59","59"),
                        ("60","60"),
                        ("61","61"),
                        ("62","62"),
                        ("63","63"),
                        ("64","64"),
                        ("65","65"),
                        ("66","66"),
                        ("67","67"),
                        ("68","68"),
                        ("69","69"),
                        ("70","70"),
                        ("71","71"),
                        ("72","72"),
                        ("73","73"),
                        ("74","74"),
                        ("75","75"),
                        ("76","76"),
                        ("77","77"),
                        ("78","78"),
                        ("79","79"),
                        ("80","80"),
                        ("81","81"),
                        ("82","82"),
                        ("83","83"),
                        ("84","84"),
                        ("85","85"),
                        ("86","86"),
                        ("87","87"),
                        ("88","88"),
                        ("89","89"),
                        ("90","90"),
                        ("91","91"),
                        ("92","92"),
                        ("93","93"),
                        ("94","94"),
                        ("95","95"),
                        ("96","96"),
                        ("97","97"),
                        ("98","98"),
                        ("99","99"),
                        ("100","100")

                    )
class FormularioNombreVariables(forms.Form):
    variable1 = forms.CharField(label='Variable 1', max_length=100, required=False)
    num_variable1 = forms.ChoiceField(choices=numero_variables, required=False)

    variable2 = forms.CharField(label='Variable 2', max_length=100, required=False)
    num_variable2 = forms.ChoiceField(choices=numero_variables, required=False)

    variable3 = forms.CharField(label='Variable 3', max_length=100, required=False)
    num_variable3 = forms.ChoiceField(choices=numero_variables, required=False)

    variable4 = forms.CharField(label='Variable 4', max_length=100, required=False)
    num_variable4 = forms.ChoiceField(choices=numero_variables, required=False)

    variable5 = forms.CharField(label='Variable 5', max_length=100, required=False)
    num_variable5 = forms.ChoiceField(choices=numero_variables, required=False)

    variable6 = forms.CharField(label='Variable 6', max_length=100, required=False)
    num_variable6 = forms.ChoiceField(choices=numero_variables, required=False)

    variable7 = forms.CharField(label='Variable 7', max_length=100, required=False)
    num_variable7 = forms.ChoiceField(choices=numero_variables, required=False)

    variable8 = forms.CharField(label='Variable 8', max_length=100, required=False)
    num_variable8 = forms.ChoiceField(choices=numero_variables, required=False)

    variable9 = forms.CharField(label='Variable 9', max_length=100, required=False)
    num_variable9 = forms.ChoiceField(choices=numero_variables, required=False)

    variable10 = forms.CharField(label='Variable 10', max_length=100, required=False)
    num_variable10 = forms.ChoiceField(choices=numero_variables, required=False)

    variable11 = forms.CharField(label='Variable 11', max_length=100, required=False)
    num_variable11 = forms.ChoiceField(choices=numero_variables, required=False)

    variable12 = forms.CharField(label='Variable 12', max_length=100, required=False)
    num_variable12 = forms.ChoiceField(choices=numero_variables, required=False)

    variable13 = forms.CharField(label='Variable 13', max_length=100, required=False)
    num_variable13 = forms.ChoiceField(choices=numero_variables, required=False)

    variable14 = forms.CharField(label='Variable 14', max_length=100, required=False)
    num_variable14 = forms.ChoiceField(choices=numero_variables, required=False)

    variable15 = forms.CharField(label='Variable 15', max_length=100, required=False)
    num_variable15 = forms.ChoiceField(choices=numero_variables, required=False)

    variable16 = forms.CharField(label='Variable 16', max_length=100, required=False)
    num_variable16 = forms.ChoiceField(choices=numero_variables, required=False)

    variable17 = forms.CharField(label='Variable 17', max_length=100, required=False)
    num_variable17 = forms.ChoiceField(choices=numero_variables, required=False)

    variable18 = forms.CharField(label='Variable 18', max_length=100, required=False)
    num_variable18 = forms.ChoiceField(choices=numero_variables, required=False)

    variable19 = forms.CharField(label='Variable 19', max_length=100, required=False)
    num_variable19 = forms.ChoiceField(choices=numero_variables, required=False)

    variable20 = forms.CharField(label='Variable 20', max_length=100, required=False)
    num_variable20 = forms.ChoiceField(choices=numero_variables, required=False)

    arb_esc = forms.ChoiceField(choices=numero_puntos, required=True)
    hectarias = forms.IntegerField(label="Distancia de los marcadores por hectaria", required=True, min_value=1)
    
class FormularioVariables(forms.Form):
    #varible 1
    var1_1 = forms.FloatField(label='Variable 1.1', required=False)
    var1_2 = forms.FloatField(label='Variable 1.2', required=False)
    var1_3 = forms.FloatField(label='Variable 1.3', required=False)
    var1_4 = forms.FloatField(label='Variable 1.4', required=False)
    var1_5 = forms.FloatField(label='Variable 1.5', required=False)
    var1_6 = forms.FloatField(label='Variable 1.6', required=False)
    var1_7 = forms.FloatField(label='Variable 1.7', required=False)
    var1_8 = forms.FloatField(label='Variable 1.8', required=False)
    var1_9 = forms.FloatField(label='Variable 1.9', required=False)
    var1_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var2_1 = forms.FloatField(label='Variable 2.1', required=False)
    var2_2 = forms.FloatField(label='Variable 2.2', required=False)
    var2_3 = forms.FloatField(label='Variable 2.3', required=False)
    var2_4 = forms.FloatField(label='Variable 2.4', required=False)
    var2_5 = forms.FloatField(label='Variable 2.5', required=False)
    var2_6 = forms.FloatField(label='Variable 2.6', required=False)
    var2_7 = forms.FloatField(label='Variable 2.7', required=False)
    var2_8 = forms.FloatField(label='Variable 2.8', required=False)
    var2_9 = forms.FloatField(label='Variable 2.9', required=False)
    var2_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var3_1 = forms.FloatField(label='Variable 3.1', required=False)
    var3_2 = forms.FloatField(label='Variable 3.2', required=False)
    var3_3 = forms.FloatField(label='Variable 3.3', required=False)
    var3_4 = forms.FloatField(label='Variable 3.4', required=False)
    var3_5 = forms.FloatField(label='Variable 3.5', required=False)
    var3_6 = forms.FloatField(label='Variable 3.6', required=False)
    var3_7 = forms.FloatField(label='Variable 3.7', required=False)
    var3_8 = forms.FloatField(label='Variable 3.8', required=False)
    var3_9 = forms.FloatField(label='Variable 3.9', required=False)
    var3_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var4_1 = forms.FloatField(label='Variable 4.1', required=False)
    var4_2 = forms.FloatField(label='Variable 4.2', required=False)
    var4_3 = forms.FloatField(label='Variable 4.3', required=False)
    var4_4 = forms.FloatField(label='Variable 4.4', required=False)
    var4_5 = forms.FloatField(label='Variable 4.5', required=False)
    var4_6 = forms.FloatField(label='Variable 4.6', required=False)
    var4_7 = forms.FloatField(label='Variable 4.7', required=False)
    var4_8 = forms.FloatField(label='Variable 4.8', required=False)
    var4_9 = forms.FloatField(label='Variable 4.9', required=False)
    var4_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var5_1 = forms.FloatField(label='Variable 5.1', required=False)
    var5_2 = forms.FloatField(label='Variable 5.2', required=False)
    var5_3 = forms.FloatField(label='Variable 5.3', required=False)
    var5_4 = forms.FloatField(label='Variable 5.4', required=False)
    var5_5 = forms.FloatField(label='Variable 5.5', required=False)
    var5_6 = forms.FloatField(label='Variable 5.6', required=False)
    var5_7 = forms.FloatField(label='Variable 5.7', required=False)
    var5_8 = forms.FloatField(label='Variable 5.8', required=False)
    var5_9 = forms.FloatField(label='Variable 5.9', required=False)
    var5_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var6_1 = forms.FloatField(label='Variable 6.1', required=False)
    var6_2 = forms.FloatField(label='Variable 6.2', required=False)
    var6_3 = forms.FloatField(label='Variable 6.3', required=False)
    var6_4 = forms.FloatField(label='Variable 6.4', required=False)
    var6_5 = forms.FloatField(label='Variable 6.5', required=False)
    var6_6 = forms.FloatField(label='Variable 6.6', required=False)
    var6_7 = forms.FloatField(label='Variable 6.7', required=False)
    var6_8 = forms.FloatField(label='Variable 6.8', required=False)
    var6_9 = forms.FloatField(label='Variable 6.9', required=False)
    var6_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var7_1 = forms.FloatField(label='Variable 7.1', required=False)
    var7_2 = forms.FloatField(label='Variable 7.2', required=False)
    var7_3 = forms.FloatField(label='Variable 7.3', required=False)
    var7_4 = forms.FloatField(label='Variable 7.4', required=False)
    var7_5 = forms.FloatField(label='Variable 7.5', required=False)
    var7_6 = forms.FloatField(label='Variable 7.6', required=False)
    var7_7 = forms.FloatField(label='Variable 7.7', required=False)
    var7_8 = forms.FloatField(label='Variable 7.8', required=False)
    var7_9 = forms.FloatField(label='Variable 7.9', required=False)
    var7_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var8_1 = forms.FloatField(label='Variable 8.1', required=False)
    var8_2 = forms.FloatField(label='Variable 8.2', required=False)
    var8_3 = forms.FloatField(label='Variable 8.3', required=False)
    var8_4 = forms.FloatField(label='Variable 8.4', required=False)
    var8_5 = forms.FloatField(label='Variable 8.5', required=False)
    var8_6 = forms.FloatField(label='Variable 8.6', required=False)
    var8_7 = forms.FloatField(label='Variable 8.7', required=False)
    var8_8 = forms.FloatField(label='Variable 8.8', required=False)
    var8_9 = forms.FloatField(label='Variable 8.9', required=False)
    var8_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var9_1 = forms.FloatField(label='Variable 9.1', required=False)
    var9_2 = forms.FloatField(label='Variable 9.2', required=False)
    var9_3 = forms.FloatField(label='Variable 9.3', required=False)
    var9_4 = forms.FloatField(label='Variable 9.4', required=False)
    var9_5 = forms.FloatField(label='Variable 9.5', required=False)
    var9_6 = forms.FloatField(label='Variable 9.6', required=False)
    var9_7 = forms.FloatField(label='Variable 9.7', required=False)
    var9_8 = forms.FloatField(label='Variable 9.8', required=False)
    var9_9 = forms.FloatField(label='Variable 9.9', required=False)
    var9_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var10_1 = forms.FloatField(label='Variable 10.1', required=False)
    var10_2 = forms.FloatField(label='Variable 10.2', required=False)
    var10_3 = forms.FloatField(label='Variable 10.3', required=False)
    var10_4 = forms.FloatField(label='Variable 10.4', required=False)
    var10_5 = forms.FloatField(label='Variable 10.5', required=False)
    var10_6 = forms.FloatField(label='Variable 10.6', required=False)
    var10_7 = forms.FloatField(label='Variable 10.7', required=False)
    var10_8 = forms.FloatField(label='Variable 10.8', required=False)
    var10_9 = forms.FloatField(label='Variable 10.9', required=False)
    var10_10 = forms.FloatField(label='Variable 10.10', required=False)

    var11_1 = forms.FloatField(label='Variable 1.1', required=False)
    var11_2 = forms.FloatField(label='Variable 1.2', required=False)
    var11_3 = forms.FloatField(label='Variable 1.3', required=False)
    var11_4 = forms.FloatField(label='Variable 1.4', required=False)
    var11_5 = forms.FloatField(label='Variable 1.5', required=False)
    var11_6 = forms.FloatField(label='Variable 1.6', required=False)
    var11_7 = forms.FloatField(label='Variable 1.7', required=False)
    var11_8 = forms.FloatField(label='Variable 1.8', required=False)
    var11_9 = forms.FloatField(label='Variable 1.9', required=False)
    var11_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var12_1 = forms.FloatField(label='Variable 2.1', required=False)
    var12_2 = forms.FloatField(label='Variable 2.2', required=False)
    var12_3 = forms.FloatField(label='Variable 2.3', required=False)
    var12_4 = forms.FloatField(label='Variable 2.4', required=False)
    var12_5 = forms.FloatField(label='Variable 2.5', required=False)
    var12_6 = forms.FloatField(label='Variable 2.6', required=False)
    var12_7 = forms.FloatField(label='Variable 2.7', required=False)
    var12_8 = forms.FloatField(label='Variable 2.8', required=False)
    var12_9 = forms.FloatField(label='Variable 2.9', required=False)
    var12_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var13_1 = forms.FloatField(label='Variable 3.1', required=False)
    var13_2 = forms.FloatField(label='Variable 3.2', required=False)
    var13_3 = forms.FloatField(label='Variable 3.3', required=False)
    var13_4 = forms.FloatField(label='Variable 3.4', required=False)
    var13_5 = forms.FloatField(label='Variable 3.5', required=False)
    var13_6 = forms.FloatField(label='Variable 3.6', required=False)
    var13_7 = forms.FloatField(label='Variable 3.7', required=False)
    var13_8 = forms.FloatField(label='Variable 3.8', required=False)
    var13_9 = forms.FloatField(label='Variable 3.9', required=False)
    var13_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var14_1 = forms.FloatField(label='Variable 4.1', required=False)
    var14_2 = forms.FloatField(label='Variable 4.2', required=False)
    var14_3 = forms.FloatField(label='Variable 4.3', required=False)
    var14_4 = forms.FloatField(label='Variable 4.4', required=False)
    var14_5 = forms.FloatField(label='Variable 4.5', required=False)
    var14_6 = forms.FloatField(label='Variable 4.6', required=False)
    var14_7 = forms.FloatField(label='Variable 4.7', required=False)
    var14_8 = forms.FloatField(label='Variable 4.8', required=False)
    var14_9 = forms.FloatField(label='Variable 4.9', required=False)
    var14_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var15_1 = forms.FloatField(label='Variable 5.1', required=False)
    var15_2 = forms.FloatField(label='Variable 5.2', required=False)
    var15_3 = forms.FloatField(label='Variable 5.3', required=False)
    var15_4 = forms.FloatField(label='Variable 5.4', required=False)
    var15_5 = forms.FloatField(label='Variable 5.5', required=False)
    var15_6 = forms.FloatField(label='Variable 5.6', required=False)
    var15_7 = forms.FloatField(label='Variable 5.7', required=False)
    var15_8 = forms.FloatField(label='Variable 5.8', required=False)
    var15_9 = forms.FloatField(label='Variable 5.9', required=False)
    var15_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var16_1 = forms.FloatField(label='Variable 6.1', required=False)
    var16_2 = forms.FloatField(label='Variable 6.2', required=False)
    var16_3 = forms.FloatField(label='Variable 6.3', required=False)
    var16_4 = forms.FloatField(label='Variable 6.4', required=False)
    var16_5 = forms.FloatField(label='Variable 6.5', required=False)
    var16_6 = forms.FloatField(label='Variable 6.6', required=False)
    var16_7 = forms.FloatField(label='Variable 6.7', required=False)
    var16_8 = forms.FloatField(label='Variable 6.8', required=False)
    var16_9 = forms.FloatField(label='Variable 6.9', required=False)
    var16_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var17_1 = forms.FloatField(label='Variable 7.1', required=False)
    var17_2 = forms.FloatField(label='Variable 7.2', required=False)
    var17_3 = forms.FloatField(label='Variable 7.3', required=False)
    var17_4 = forms.FloatField(label='Variable 7.4', required=False)
    var17_5 = forms.FloatField(label='Variable 7.5', required=False)
    var17_6 = forms.FloatField(label='Variable 7.6', required=False)
    var17_7 = forms.FloatField(label='Variable 7.7', required=False)
    var17_8 = forms.FloatField(label='Variable 7.8', required=False)
    var17_9 = forms.FloatField(label='Variable 7.9', required=False)
    var17_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var18_1 = forms.FloatField(label='Variable 8.1', required=False)
    var18_2 = forms.FloatField(label='Variable 8.2', required=False)
    var18_3 = forms.FloatField(label='Variable 8.3', required=False)
    var18_4 = forms.FloatField(label='Variable 8.4', required=False)
    var18_5 = forms.FloatField(label='Variable 8.5', required=False)
    var18_6 = forms.FloatField(label='Variable 8.6', required=False)
    var18_7 = forms.FloatField(label='Variable 8.7', required=False)
    var18_8 = forms.FloatField(label='Variable 8.8', required=False)
    var18_9 = forms.FloatField(label='Variable 8.9', required=False)
    var18_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var19_1 = forms.FloatField(label='Variable 9.1', required=False)
    var19_2 = forms.FloatField(label='Variable 9.2', required=False)
    var19_3 = forms.FloatField(label='Variable 9.3', required=False)
    var19_4 = forms.FloatField(label='Variable 9.4', required=False)
    var19_5 = forms.FloatField(label='Variable 9.5', required=False)
    var19_6 = forms.FloatField(label='Variable 9.6', required=False)
    var19_7 = forms.FloatField(label='Variable 9.7', required=False)
    var19_8 = forms.FloatField(label='Variable 9.8', required=False)
    var19_9 = forms.FloatField(label='Variable 9.9', required=False)
    var19_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var20_1 = forms.FloatField(label='Variable 10.1', required=False)
    var20_2 = forms.FloatField(label='Variable 10.2', required=False)
    var20_3 = forms.FloatField(label='Variable 10.3', required=False)
    var20_4 = forms.FloatField(label='Variable 10.4', required=False)
    var20_5 = forms.FloatField(label='Variable 10.5', required=False)
    var20_6 = forms.FloatField(label='Variable 10.6', required=False)
    var20_7 = forms.FloatField(label='Variable 10.7', required=False)
    var20_8 = forms.FloatField(label='Variable 10.8', required=False)
    var20_9 = forms.FloatField(label='Variable 10.9', required=False)
    var20_10 = forms.FloatField(label='Variable 10.10', required=False)

    var21_1 = forms.FloatField(label='Variable 1.1', required=False)
    var21_2 = forms.FloatField(label='Variable 1.2', required=False)
    var21_3 = forms.FloatField(label='Variable 1.3', required=False)
    var21_4 = forms.FloatField(label='Variable 1.4', required=False)
    var21_5 = forms.FloatField(label='Variable 1.5', required=False)
    var21_6 = forms.FloatField(label='Variable 1.6', required=False)
    var21_7 = forms.FloatField(label='Variable 1.7', required=False)
    var21_8 = forms.FloatField(label='Variable 1.8', required=False)
    var21_9 = forms.FloatField(label='Variable 1.9', required=False)
    var21_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var22_1 = forms.FloatField(label='Variable 2.1', required=False)
    var22_2 = forms.FloatField(label='Variable 2.2', required=False)
    var22_3 = forms.FloatField(label='Variable 2.3', required=False)
    var22_4 = forms.FloatField(label='Variable 2.4', required=False)
    var22_5 = forms.FloatField(label='Variable 2.5', required=False)
    var22_6 = forms.FloatField(label='Variable 2.6', required=False)
    var22_7 = forms.FloatField(label='Variable 2.7', required=False)
    var22_8 = forms.FloatField(label='Variable 2.8', required=False)
    var22_9 = forms.FloatField(label='Variable 2.9', required=False)
    var22_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var23_1 = forms.FloatField(label='Variable 3.1', required=False)
    var23_2 = forms.FloatField(label='Variable 3.2', required=False)
    var23_3 = forms.FloatField(label='Variable 3.3', required=False)
    var23_4 = forms.FloatField(label='Variable 3.4', required=False)
    var23_5 = forms.FloatField(label='Variable 3.5', required=False)
    var23_6 = forms.FloatField(label='Variable 3.6', required=False)
    var23_7 = forms.FloatField(label='Variable 3.7', required=False)
    var23_8 = forms.FloatField(label='Variable 3.8', required=False)
    var23_9 = forms.FloatField(label='Variable 3.9', required=False)
    var23_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var24_1 = forms.FloatField(label='Variable 4.1', required=False)
    var24_2 = forms.FloatField(label='Variable 4.2', required=False)
    var24_3 = forms.FloatField(label='Variable 4.3', required=False)
    var24_4 = forms.FloatField(label='Variable 4.4', required=False)
    var24_5 = forms.FloatField(label='Variable 4.5', required=False)
    var24_6 = forms.FloatField(label='Variable 4.6', required=False)
    var24_7 = forms.FloatField(label='Variable 4.7', required=False)
    var24_8 = forms.FloatField(label='Variable 4.8', required=False)
    var24_9 = forms.FloatField(label='Variable 4.9', required=False)
    var24_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var25_1 = forms.FloatField(label='Variable 5.1', required=False)
    var25_2 = forms.FloatField(label='Variable 5.2', required=False)
    var25_3 = forms.FloatField(label='Variable 5.3', required=False)
    var25_4 = forms.FloatField(label='Variable 5.4', required=False)
    var25_5 = forms.FloatField(label='Variable 5.5', required=False)
    var25_6 = forms.FloatField(label='Variable 5.6', required=False)
    var25_7 = forms.FloatField(label='Variable 5.7', required=False)
    var25_8 = forms.FloatField(label='Variable 5.8', required=False)
    var25_9 = forms.FloatField(label='Variable 5.9', required=False)
    var25_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var26_1 = forms.FloatField(label='Variable 6.1', required=False)
    var26_2 = forms.FloatField(label='Variable 6.2', required=False)
    var26_3 = forms.FloatField(label='Variable 6.3', required=False)
    var26_4 = forms.FloatField(label='Variable 6.4', required=False)
    var26_5 = forms.FloatField(label='Variable 6.5', required=False)
    var26_6 = forms.FloatField(label='Variable 6.6', required=False)
    var26_7 = forms.FloatField(label='Variable 6.7', required=False)
    var26_8 = forms.FloatField(label='Variable 6.8', required=False)
    var26_9 = forms.FloatField(label='Variable 6.9', required=False)
    var26_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var27_1 = forms.FloatField(label='Variable 7.1', required=False)
    var27_2 = forms.FloatField(label='Variable 7.2', required=False)
    var27_3 = forms.FloatField(label='Variable 7.3', required=False)
    var27_4 = forms.FloatField(label='Variable 7.4', required=False)
    var27_5 = forms.FloatField(label='Variable 7.5', required=False)
    var27_6 = forms.FloatField(label='Variable 7.6', required=False)
    var27_7 = forms.FloatField(label='Variable 7.7', required=False)
    var27_8 = forms.FloatField(label='Variable 7.8', required=False)
    var27_9 = forms.FloatField(label='Variable 7.9', required=False)
    var27_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var28_1 = forms.FloatField(label='Variable 8.1', required=False)
    var28_2 = forms.FloatField(label='Variable 8.2', required=False)
    var28_3 = forms.FloatField(label='Variable 8.3', required=False)
    var28_4 = forms.FloatField(label='Variable 8.4', required=False)
    var28_5 = forms.FloatField(label='Variable 8.5', required=False)
    var28_6 = forms.FloatField(label='Variable 8.6', required=False)
    var28_7 = forms.FloatField(label='Variable 8.7', required=False)
    var28_8 = forms.FloatField(label='Variable 8.8', required=False)
    var28_9 = forms.FloatField(label='Variable 8.9', required=False)
    var28_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var29_1 = forms.FloatField(label='Variable 9.1', required=False)
    var29_2 = forms.FloatField(label='Variable 9.2', required=False)
    var29_3 = forms.FloatField(label='Variable 9.3', required=False)
    var29_4 = forms.FloatField(label='Variable 9.4', required=False)
    var29_5 = forms.FloatField(label='Variable 9.5', required=False)
    var29_6 = forms.FloatField(label='Variable 9.6', required=False)
    var29_7 = forms.FloatField(label='Variable 9.7', required=False)
    var29_8 = forms.FloatField(label='Variable 9.8', required=False)
    var29_9 = forms.FloatField(label='Variable 9.9', required=False)
    var29_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var30_1 = forms.FloatField(label='Variable 10.1', required=False)
    var30_2 = forms.FloatField(label='Variable 10.2', required=False)
    var30_3 = forms.FloatField(label='Variable 10.3', required=False)
    var30_4 = forms.FloatField(label='Variable 10.4', required=False)
    var30_5 = forms.FloatField(label='Variable 10.5', required=False)
    var30_6 = forms.FloatField(label='Variable 10.6', required=False)
    var30_7 = forms.FloatField(label='Variable 10.7', required=False)
    var30_8 = forms.FloatField(label='Variable 10.8', required=False)
    var30_9 = forms.FloatField(label='Variable 10.9', required=False)
    var30_10 = forms.FloatField(label='Variable 10.10', required=False)

    var31_1 = forms.FloatField(label='Variable 1.1', required=False)
    var31_2 = forms.FloatField(label='Variable 1.2', required=False)
    var31_3 = forms.FloatField(label='Variable 1.3', required=False)
    var31_4 = forms.FloatField(label='Variable 1.4', required=False)
    var31_5 = forms.FloatField(label='Variable 1.5', required=False)
    var31_6 = forms.FloatField(label='Variable 1.6', required=False)
    var31_7 = forms.FloatField(label='Variable 1.7', required=False)
    var31_8 = forms.FloatField(label='Variable 1.8', required=False)
    var31_9 = forms.FloatField(label='Variable 1.9', required=False)
    var31_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var32_1 = forms.FloatField(label='Variable 2.1', required=False)
    var32_2 = forms.FloatField(label='Variable 2.2', required=False)
    var32_3 = forms.FloatField(label='Variable 2.3', required=False)
    var32_4 = forms.FloatField(label='Variable 2.4', required=False)
    var32_5 = forms.FloatField(label='Variable 2.5', required=False)
    var32_6 = forms.FloatField(label='Variable 2.6', required=False)
    var32_7 = forms.FloatField(label='Variable 2.7', required=False)
    var32_8 = forms.FloatField(label='Variable 2.8', required=False)
    var32_9 = forms.FloatField(label='Variable 2.9', required=False)
    var32_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var33_1 = forms.FloatField(label='Variable 3.1', required=False)
    var33_2 = forms.FloatField(label='Variable 3.2', required=False)
    var33_3 = forms.FloatField(label='Variable 3.3', required=False)
    var33_4 = forms.FloatField(label='Variable 3.4', required=False)
    var33_5 = forms.FloatField(label='Variable 3.5', required=False)
    var33_6 = forms.FloatField(label='Variable 3.6', required=False)
    var33_7 = forms.FloatField(label='Variable 3.7', required=False)
    var33_8 = forms.FloatField(label='Variable 3.8', required=False)
    var33_9 = forms.FloatField(label='Variable 3.9', required=False)
    var33_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var34_1 = forms.FloatField(label='Variable 4.1', required=False)
    var34_2 = forms.FloatField(label='Variable 4.2', required=False)
    var34_3 = forms.FloatField(label='Variable 4.3', required=False)
    var34_4 = forms.FloatField(label='Variable 4.4', required=False)
    var34_5 = forms.FloatField(label='Variable 4.5', required=False)
    var34_6 = forms.FloatField(label='Variable 4.6', required=False)
    var34_7 = forms.FloatField(label='Variable 4.7', required=False)
    var34_8 = forms.FloatField(label='Variable 4.8', required=False)
    var34_9 = forms.FloatField(label='Variable 4.9', required=False)
    var34_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var35_1 = forms.FloatField(label='Variable 5.1', required=False)
    var35_2 = forms.FloatField(label='Variable 5.2', required=False)
    var35_3 = forms.FloatField(label='Variable 5.3', required=False)
    var35_4 = forms.FloatField(label='Variable 5.4', required=False)
    var35_5 = forms.FloatField(label='Variable 5.5', required=False)
    var35_6 = forms.FloatField(label='Variable 5.6', required=False)
    var35_7 = forms.FloatField(label='Variable 5.7', required=False)
    var35_8 = forms.FloatField(label='Variable 5.8', required=False)
    var35_9 = forms.FloatField(label='Variable 5.9', required=False)
    var35_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var36_1 = forms.FloatField(label='Variable 6.1', required=False)
    var36_2 = forms.FloatField(label='Variable 6.2', required=False)
    var36_3 = forms.FloatField(label='Variable 6.3', required=False)
    var36_4 = forms.FloatField(label='Variable 6.4', required=False)
    var36_5 = forms.FloatField(label='Variable 6.5', required=False)
    var36_6 = forms.FloatField(label='Variable 6.6', required=False)
    var36_7 = forms.FloatField(label='Variable 6.7', required=False)
    var36_8 = forms.FloatField(label='Variable 6.8', required=False)
    var36_9 = forms.FloatField(label='Variable 6.9', required=False)
    var36_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var37_1 = forms.FloatField(label='Variable 7.1', required=False)
    var37_2 = forms.FloatField(label='Variable 7.2', required=False)
    var37_3 = forms.FloatField(label='Variable 7.3', required=False)
    var37_4 = forms.FloatField(label='Variable 7.4', required=False)
    var37_5 = forms.FloatField(label='Variable 7.5', required=False)
    var37_6 = forms.FloatField(label='Variable 7.6', required=False)
    var37_7 = forms.FloatField(label='Variable 7.7', required=False)
    var37_8 = forms.FloatField(label='Variable 7.8', required=False)
    var37_9 = forms.FloatField(label='Variable 7.9', required=False)
    var37_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var38_1 = forms.FloatField(label='Variable 8.1', required=False)
    var38_2 = forms.FloatField(label='Variable 8.2', required=False)
    var38_3 = forms.FloatField(label='Variable 8.3', required=False)
    var38_4 = forms.FloatField(label='Variable 8.4', required=False)
    var38_5 = forms.FloatField(label='Variable 8.5', required=False)
    var38_6 = forms.FloatField(label='Variable 8.6', required=False)
    var38_7 = forms.FloatField(label='Variable 8.7', required=False)
    var38_8 = forms.FloatField(label='Variable 8.8', required=False)
    var38_9 = forms.FloatField(label='Variable 8.9', required=False)
    var38_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var39_1 = forms.FloatField(label='Variable 9.1', required=False)
    var39_2 = forms.FloatField(label='Variable 9.2', required=False)
    var39_3 = forms.FloatField(label='Variable 9.3', required=False)
    var39_4 = forms.FloatField(label='Variable 9.4', required=False)
    var39_5 = forms.FloatField(label='Variable 9.5', required=False)
    var39_6 = forms.FloatField(label='Variable 9.6', required=False)
    var39_7 = forms.FloatField(label='Variable 9.7', required=False)
    var39_8 = forms.FloatField(label='Variable 9.8', required=False)
    var39_9 = forms.FloatField(label='Variable 9.9', required=False)
    var39_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var40_1 = forms.FloatField(label='Variable 10.1', required=False)
    var40_2 = forms.FloatField(label='Variable 10.2', required=False)
    var40_3 = forms.FloatField(label='Variable 10.3', required=False)
    var40_4 = forms.FloatField(label='Variable 10.4', required=False)
    var40_5 = forms.FloatField(label='Variable 10.5', required=False)
    var40_6 = forms.FloatField(label='Variable 10.6', required=False)
    var40_7 = forms.FloatField(label='Variable 10.7', required=False)
    var40_8 = forms.FloatField(label='Variable 10.8', required=False)
    var40_9 = forms.FloatField(label='Variable 10.9', required=False)
    var40_10 = forms.FloatField(label='Variable 10.10', required=False)

    var41_1 = forms.FloatField(label='Variable 1.1', required=False)
    var41_2 = forms.FloatField(label='Variable 1.2', required=False)
    var41_3 = forms.FloatField(label='Variable 1.3', required=False)
    var41_4 = forms.FloatField(label='Variable 1.4', required=False)
    var41_5 = forms.FloatField(label='Variable 1.5', required=False)
    var41_6 = forms.FloatField(label='Variable 1.6', required=False)
    var41_7 = forms.FloatField(label='Variable 1.7', required=False)
    var41_8 = forms.FloatField(label='Variable 1.8', required=False)
    var41_9 = forms.FloatField(label='Variable 1.9', required=False)
    var41_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var42_1 = forms.FloatField(label='Variable 2.1', required=False)
    var42_2 = forms.FloatField(label='Variable 2.2', required=False)
    var42_3 = forms.FloatField(label='Variable 2.3', required=False)
    var42_4 = forms.FloatField(label='Variable 2.4', required=False)
    var42_5 = forms.FloatField(label='Variable 2.5', required=False)
    var42_6 = forms.FloatField(label='Variable 2.6', required=False)
    var42_7 = forms.FloatField(label='Variable 2.7', required=False)
    var42_8 = forms.FloatField(label='Variable 2.8', required=False)
    var42_9 = forms.FloatField(label='Variable 2.9', required=False)
    var42_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var43_1 = forms.FloatField(label='Variable 3.1', required=False)
    var43_2 = forms.FloatField(label='Variable 3.2', required=False)
    var43_3 = forms.FloatField(label='Variable 3.3', required=False)
    var43_4 = forms.FloatField(label='Variable 3.4', required=False)
    var43_5 = forms.FloatField(label='Variable 3.5', required=False)
    var43_6 = forms.FloatField(label='Variable 3.6', required=False)
    var43_7 = forms.FloatField(label='Variable 3.7', required=False)
    var43_8 = forms.FloatField(label='Variable 3.8', required=False)
    var43_9 = forms.FloatField(label='Variable 3.9', required=False)
    var43_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var44_1 = forms.FloatField(label='Variable 4.1', required=False)
    var44_2 = forms.FloatField(label='Variable 4.2', required=False)
    var44_3 = forms.FloatField(label='Variable 4.3', required=False)
    var44_4 = forms.FloatField(label='Variable 4.4', required=False)
    var44_5 = forms.FloatField(label='Variable 4.5', required=False)
    var44_6 = forms.FloatField(label='Variable 4.6', required=False)
    var44_7 = forms.FloatField(label='Variable 4.7', required=False)
    var44_8 = forms.FloatField(label='Variable 4.8', required=False)
    var44_9 = forms.FloatField(label='Variable 4.9', required=False)
    var44_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var45_1 = forms.FloatField(label='Variable 5.1', required=False)
    var45_2 = forms.FloatField(label='Variable 5.2', required=False)
    var45_3 = forms.FloatField(label='Variable 5.3', required=False)
    var45_4 = forms.FloatField(label='Variable 5.4', required=False)
    var45_5 = forms.FloatField(label='Variable 5.5', required=False)
    var45_6 = forms.FloatField(label='Variable 5.6', required=False)
    var45_7 = forms.FloatField(label='Variable 5.7', required=False)
    var45_8 = forms.FloatField(label='Variable 5.8', required=False)
    var45_9 = forms.FloatField(label='Variable 5.9', required=False)
    var45_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var46_1 = forms.FloatField(label='Variable 6.1', required=False)
    var46_2 = forms.FloatField(label='Variable 6.2', required=False)
    var46_3 = forms.FloatField(label='Variable 6.3', required=False)
    var46_4 = forms.FloatField(label='Variable 6.4', required=False)
    var46_5 = forms.FloatField(label='Variable 6.5', required=False)
    var46_6 = forms.FloatField(label='Variable 6.6', required=False)
    var46_7 = forms.FloatField(label='Variable 6.7', required=False)
    var46_8 = forms.FloatField(label='Variable 6.8', required=False)
    var46_9 = forms.FloatField(label='Variable 6.9', required=False)
    var46_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var47_1 = forms.FloatField(label='Variable 7.1', required=False)
    var47_2 = forms.FloatField(label='Variable 7.2', required=False)
    var47_3 = forms.FloatField(label='Variable 7.3', required=False)
    var47_4 = forms.FloatField(label='Variable 7.4', required=False)
    var47_5 = forms.FloatField(label='Variable 7.5', required=False)
    var47_6 = forms.FloatField(label='Variable 7.6', required=False)
    var47_7 = forms.FloatField(label='Variable 7.7', required=False)
    var47_8 = forms.FloatField(label='Variable 7.8', required=False)
    var47_9 = forms.FloatField(label='Variable 7.9', required=False)
    var47_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var48_1 = forms.FloatField(label='Variable 8.1', required=False)
    var48_2 = forms.FloatField(label='Variable 8.2', required=False)
    var48_3 = forms.FloatField(label='Variable 8.3', required=False)
    var48_4 = forms.FloatField(label='Variable 8.4', required=False)
    var48_5 = forms.FloatField(label='Variable 8.5', required=False)
    var48_6 = forms.FloatField(label='Variable 8.6', required=False)
    var48_7 = forms.FloatField(label='Variable 8.7', required=False)
    var48_8 = forms.FloatField(label='Variable 8.8', required=False)
    var48_9 = forms.FloatField(label='Variable 8.9', required=False)
    var48_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var49_1 = forms.FloatField(label='Variable 9.1', required=False)
    var49_2 = forms.FloatField(label='Variable 9.2', required=False)
    var49_3 = forms.FloatField(label='Variable 9.3', required=False)
    var49_4 = forms.FloatField(label='Variable 9.4', required=False)
    var49_5 = forms.FloatField(label='Variable 9.5', required=False)
    var49_6 = forms.FloatField(label='Variable 9.6', required=False)
    var49_7 = forms.FloatField(label='Variable 9.7', required=False)
    var49_8 = forms.FloatField(label='Variable 9.8', required=False)
    var49_9 = forms.FloatField(label='Variable 9.9', required=False)
    var49_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var50_1 = forms.FloatField(label='Variable 10.1', required=False)
    var50_2 = forms.FloatField(label='Variable 10.2', required=False)
    var50_3 = forms.FloatField(label='Variable 10.3', required=False)
    var50_4 = forms.FloatField(label='Variable 10.4', required=False)
    var50_5 = forms.FloatField(label='Variable 10.5', required=False)
    var50_6 = forms.FloatField(label='Variable 10.6', required=False)
    var50_7 = forms.FloatField(label='Variable 10.7', required=False)
    var50_8 = forms.FloatField(label='Variable 10.8', required=False)
    var50_9 = forms.FloatField(label='Variable 10.9', required=False)
    var50_10 = forms.FloatField(label='Variable 10.10', required=False)

    var51_1 = forms.FloatField(label='Variable 1.1', required=False)
    var51_2 = forms.FloatField(label='Variable 1.2', required=False)
    var51_3 = forms.FloatField(label='Variable 1.3', required=False)
    var51_4 = forms.FloatField(label='Variable 1.4', required=False)
    var51_5 = forms.FloatField(label='Variable 1.5', required=False)
    var51_6 = forms.FloatField(label='Variable 1.6', required=False)
    var51_7 = forms.FloatField(label='Variable 1.7', required=False)
    var51_8 = forms.FloatField(label='Variable 1.8', required=False)
    var51_9 = forms.FloatField(label='Variable 1.9', required=False)
    var51_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var52_1 = forms.FloatField(label='Variable 2.1', required=False)
    var52_2 = forms.FloatField(label='Variable 2.2', required=False)
    var52_3 = forms.FloatField(label='Variable 2.3', required=False)
    var52_4 = forms.FloatField(label='Variable 2.4', required=False)
    var52_5 = forms.FloatField(label='Variable 2.5', required=False)
    var52_6 = forms.FloatField(label='Variable 2.6', required=False)
    var52_7 = forms.FloatField(label='Variable 2.7', required=False)
    var52_8 = forms.FloatField(label='Variable 2.8', required=False)
    var52_9 = forms.FloatField(label='Variable 2.9', required=False)
    var52_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var53_1 = forms.FloatField(label='Variable 3.1', required=False)
    var53_2 = forms.FloatField(label='Variable 3.2', required=False)
    var53_3 = forms.FloatField(label='Variable 3.3', required=False)
    var53_4 = forms.FloatField(label='Variable 3.4', required=False)
    var53_5 = forms.FloatField(label='Variable 3.5', required=False)
    var53_6 = forms.FloatField(label='Variable 3.6', required=False)
    var53_7 = forms.FloatField(label='Variable 3.7', required=False)
    var53_8 = forms.FloatField(label='Variable 3.8', required=False)
    var53_9 = forms.FloatField(label='Variable 3.9', required=False)
    var53_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var54_1 = forms.FloatField(label='Variable 4.1', required=False)
    var54_2 = forms.FloatField(label='Variable 4.2', required=False)
    var54_3 = forms.FloatField(label='Variable 4.3', required=False)
    var54_4 = forms.FloatField(label='Variable 4.4', required=False)
    var54_5 = forms.FloatField(label='Variable 4.5', required=False)
    var54_6 = forms.FloatField(label='Variable 4.6', required=False)
    var54_7 = forms.FloatField(label='Variable 4.7', required=False)
    var54_8 = forms.FloatField(label='Variable 4.8', required=False)
    var54_9 = forms.FloatField(label='Variable 4.9', required=False)
    var54_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var55_1 = forms.FloatField(label='Variable 5.1', required=False)
    var55_2 = forms.FloatField(label='Variable 5.2', required=False)
    var55_3 = forms.FloatField(label='Variable 5.3', required=False)
    var55_4 = forms.FloatField(label='Variable 5.4', required=False)
    var55_5 = forms.FloatField(label='Variable 5.5', required=False)
    var55_6 = forms.FloatField(label='Variable 5.6', required=False)
    var55_7 = forms.FloatField(label='Variable 5.7', required=False)
    var55_8 = forms.FloatField(label='Variable 5.8', required=False)
    var55_9 = forms.FloatField(label='Variable 5.9', required=False)
    var55_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var56_1 = forms.FloatField(label='Variable 6.1', required=False)
    var56_2 = forms.FloatField(label='Variable 6.2', required=False)
    var56_3 = forms.FloatField(label='Variable 6.3', required=False)
    var56_4 = forms.FloatField(label='Variable 6.4', required=False)
    var56_5 = forms.FloatField(label='Variable 6.5', required=False)
    var56_6 = forms.FloatField(label='Variable 6.6', required=False)
    var56_7 = forms.FloatField(label='Variable 6.7', required=False)
    var56_8 = forms.FloatField(label='Variable 6.8', required=False)
    var56_9 = forms.FloatField(label='Variable 6.9', required=False)
    var56_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var57_1 = forms.FloatField(label='Variable 7.1', required=False)
    var57_2 = forms.FloatField(label='Variable 7.2', required=False)
    var57_3 = forms.FloatField(label='Variable 7.3', required=False)
    var57_4 = forms.FloatField(label='Variable 7.4', required=False)
    var57_5 = forms.FloatField(label='Variable 7.5', required=False)
    var57_6 = forms.FloatField(label='Variable 7.6', required=False)
    var57_7 = forms.FloatField(label='Variable 7.7', required=False)
    var57_8 = forms.FloatField(label='Variable 7.8', required=False)
    var57_9 = forms.FloatField(label='Variable 7.9', required=False)
    var57_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var58_1 = forms.FloatField(label='Variable 8.1', required=False)
    var58_2 = forms.FloatField(label='Variable 8.2', required=False)
    var58_3 = forms.FloatField(label='Variable 8.3', required=False)
    var58_4 = forms.FloatField(label='Variable 8.4', required=False)
    var58_5 = forms.FloatField(label='Variable 8.5', required=False)
    var58_6 = forms.FloatField(label='Variable 8.6', required=False)
    var58_7 = forms.FloatField(label='Variable 8.7', required=False)
    var58_8 = forms.FloatField(label='Variable 8.8', required=False)
    var58_9 = forms.FloatField(label='Variable 8.9', required=False)
    var58_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var59_1 = forms.FloatField(label='Variable 9.1', required=False)
    var59_2 = forms.FloatField(label='Variable 9.2', required=False)
    var59_3 = forms.FloatField(label='Variable 9.3', required=False)
    var59_4 = forms.FloatField(label='Variable 9.4', required=False)
    var59_5 = forms.FloatField(label='Variable 9.5', required=False)
    var59_6 = forms.FloatField(label='Variable 9.6', required=False)
    var59_7 = forms.FloatField(label='Variable 9.7', required=False)
    var59_8 = forms.FloatField(label='Variable 9.8', required=False)
    var59_9 = forms.FloatField(label='Variable 9.9', required=False)
    var59_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var60_1 = forms.FloatField(label='Variable 10.1', required=False)
    var60_2 = forms.FloatField(label='Variable 10.2', required=False)
    var60_3 = forms.FloatField(label='Variable 10.3', required=False)
    var60_4 = forms.FloatField(label='Variable 10.4', required=False)
    var60_5 = forms.FloatField(label='Variable 10.5', required=False)
    var60_6 = forms.FloatField(label='Variable 10.6', required=False)
    var60_7 = forms.FloatField(label='Variable 10.7', required=False)
    var60_8 = forms.FloatField(label='Variable 10.8', required=False)
    var60_9 = forms.FloatField(label='Variable 10.9', required=False)
    var60_10 = forms.FloatField(label='Variable 10.10', required=False)

    var61_1 = forms.FloatField(label='Variable 1.1', required=False)
    var61_2 = forms.FloatField(label='Variable 1.2', required=False)
    var61_3 = forms.FloatField(label='Variable 1.3', required=False)
    var61_4 = forms.FloatField(label='Variable 1.4', required=False)
    var61_5 = forms.FloatField(label='Variable 1.5', required=False)
    var61_6 = forms.FloatField(label='Variable 1.6', required=False)
    var61_7 = forms.FloatField(label='Variable 1.7', required=False)
    var61_8 = forms.FloatField(label='Variable 1.8', required=False)
    var61_9 = forms.FloatField(label='Variable 1.9', required=False)
    var61_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var62_1 = forms.FloatField(label='Variable 2.1', required=False)
    var62_2 = forms.FloatField(label='Variable 2.2', required=False)
    var62_3 = forms.FloatField(label='Variable 2.3', required=False)
    var62_4 = forms.FloatField(label='Variable 2.4', required=False)
    var62_5 = forms.FloatField(label='Variable 2.5', required=False)
    var62_6 = forms.FloatField(label='Variable 2.6', required=False)
    var62_7 = forms.FloatField(label='Variable 2.7', required=False)
    var62_8 = forms.FloatField(label='Variable 2.8', required=False)
    var62_9 = forms.FloatField(label='Variable 2.9', required=False)
    var62_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var63_1 = forms.FloatField(label='Variable 3.1', required=False)
    var63_2 = forms.FloatField(label='Variable 3.2', required=False)
    var63_3 = forms.FloatField(label='Variable 3.3', required=False)
    var63_4 = forms.FloatField(label='Variable 3.4', required=False)
    var63_5 = forms.FloatField(label='Variable 3.5', required=False)
    var63_6 = forms.FloatField(label='Variable 3.6', required=False)
    var63_7 = forms.FloatField(label='Variable 3.7', required=False)
    var63_8 = forms.FloatField(label='Variable 3.8', required=False)
    var63_9 = forms.FloatField(label='Variable 3.9', required=False)
    var63_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var64_1 = forms.FloatField(label='Variable 4.1', required=False)
    var64_2 = forms.FloatField(label='Variable 4.2', required=False)
    var64_3 = forms.FloatField(label='Variable 4.3', required=False)
    var64_4 = forms.FloatField(label='Variable 4.4', required=False)
    var64_5 = forms.FloatField(label='Variable 4.5', required=False)
    var64_6 = forms.FloatField(label='Variable 4.6', required=False)
    var64_7 = forms.FloatField(label='Variable 4.7', required=False)
    var64_8 = forms.FloatField(label='Variable 4.8', required=False)
    var64_9 = forms.FloatField(label='Variable 4.9', required=False)
    var64_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var65_1 = forms.FloatField(label='Variable 5.1', required=False)
    var65_2 = forms.FloatField(label='Variable 5.2', required=False)
    var65_3 = forms.FloatField(label='Variable 5.3', required=False)
    var65_4 = forms.FloatField(label='Variable 5.4', required=False)
    var65_5 = forms.FloatField(label='Variable 5.5', required=False)
    var65_6 = forms.FloatField(label='Variable 5.6', required=False)
    var65_7 = forms.FloatField(label='Variable 5.7', required=False)
    var65_8 = forms.FloatField(label='Variable 5.8', required=False)
    var65_9 = forms.FloatField(label='Variable 5.9', required=False)
    var65_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var66_1 = forms.FloatField(label='Variable 6.1', required=False)
    var66_2 = forms.FloatField(label='Variable 6.2', required=False)
    var66_3 = forms.FloatField(label='Variable 6.3', required=False)
    var66_4 = forms.FloatField(label='Variable 6.4', required=False)
    var66_5 = forms.FloatField(label='Variable 6.5', required=False)
    var66_6 = forms.FloatField(label='Variable 6.6', required=False)
    var66_7 = forms.FloatField(label='Variable 6.7', required=False)
    var66_8 = forms.FloatField(label='Variable 6.8', required=False)
    var66_9 = forms.FloatField(label='Variable 6.9', required=False)
    var66_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var67_1 = forms.FloatField(label='Variable 7.1', required=False)
    var67_2 = forms.FloatField(label='Variable 7.2', required=False)
    var67_3 = forms.FloatField(label='Variable 7.3', required=False)
    var67_4 = forms.FloatField(label='Variable 7.4', required=False)
    var67_5 = forms.FloatField(label='Variable 7.5', required=False)
    var67_6 = forms.FloatField(label='Variable 7.6', required=False)
    var67_7 = forms.FloatField(label='Variable 7.7', required=False)
    var67_8 = forms.FloatField(label='Variable 7.8', required=False)
    var67_9 = forms.FloatField(label='Variable 7.9', required=False)
    var67_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var68_1 = forms.FloatField(label='Variable 8.1', required=False)
    var68_2 = forms.FloatField(label='Variable 8.2', required=False)
    var68_3 = forms.FloatField(label='Variable 8.3', required=False)
    var68_4 = forms.FloatField(label='Variable 8.4', required=False)
    var68_5 = forms.FloatField(label='Variable 8.5', required=False)
    var68_6 = forms.FloatField(label='Variable 8.6', required=False)
    var68_7 = forms.FloatField(label='Variable 8.7', required=False)
    var68_8 = forms.FloatField(label='Variable 8.8', required=False)
    var68_9 = forms.FloatField(label='Variable 8.9', required=False)
    var68_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var69_1 = forms.FloatField(label='Variable 9.1', required=False)
    var69_2 = forms.FloatField(label='Variable 9.2', required=False)
    var69_3 = forms.FloatField(label='Variable 9.3', required=False)
    var69_4 = forms.FloatField(label='Variable 9.4', required=False)
    var69_5 = forms.FloatField(label='Variable 9.5', required=False)
    var69_6 = forms.FloatField(label='Variable 9.6', required=False)
    var69_7 = forms.FloatField(label='Variable 9.7', required=False)
    var69_8 = forms.FloatField(label='Variable 9.8', required=False)
    var69_9 = forms.FloatField(label='Variable 9.9', required=False)
    var69_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var70_1 = forms.FloatField(label='Variable 10.1', required=False)
    var70_2 = forms.FloatField(label='Variable 10.2', required=False)
    var70_3 = forms.FloatField(label='Variable 10.3', required=False)
    var70_4 = forms.FloatField(label='Variable 10.4', required=False)
    var70_5 = forms.FloatField(label='Variable 10.5', required=False)
    var70_6 = forms.FloatField(label='Variable 10.6', required=False)
    var70_7 = forms.FloatField(label='Variable 10.7', required=False)
    var70_8 = forms.FloatField(label='Variable 10.8', required=False)
    var70_9 = forms.FloatField(label='Variable 10.9', required=False)
    var70_10 = forms.FloatField(label='Variable 10.10', required=False)

    var71_1 = forms.FloatField(label='Variable 1.1', required=False)
    var71_2 = forms.FloatField(label='Variable 1.2', required=False)
    var71_3 = forms.FloatField(label='Variable 1.3', required=False)
    var71_4 = forms.FloatField(label='Variable 1.4', required=False)
    var71_5 = forms.FloatField(label='Variable 1.5', required=False)
    var71_6 = forms.FloatField(label='Variable 1.6', required=False)
    var71_7 = forms.FloatField(label='Variable 1.7', required=False)
    var71_8 = forms.FloatField(label='Variable 1.8', required=False)
    var71_9 = forms.FloatField(label='Variable 1.9', required=False)
    var71_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var72_1 = forms.FloatField(label='Variable 2.1', required=False)
    var72_2 = forms.FloatField(label='Variable 2.2', required=False)
    var72_3 = forms.FloatField(label='Variable 2.3', required=False)
    var72_4 = forms.FloatField(label='Variable 2.4', required=False)
    var72_5 = forms.FloatField(label='Variable 2.5', required=False)
    var72_6 = forms.FloatField(label='Variable 2.6', required=False)
    var72_7 = forms.FloatField(label='Variable 2.7', required=False)
    var72_8 = forms.FloatField(label='Variable 2.8', required=False)
    var72_9 = forms.FloatField(label='Variable 2.9', required=False)
    var72_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var73_1 = forms.FloatField(label='Variable 3.1', required=False)
    var73_2 = forms.FloatField(label='Variable 3.2', required=False)
    var73_3 = forms.FloatField(label='Variable 3.3', required=False)
    var73_4 = forms.FloatField(label='Variable 3.4', required=False)
    var73_5 = forms.FloatField(label='Variable 3.5', required=False)
    var73_6 = forms.FloatField(label='Variable 3.6', required=False)
    var73_7 = forms.FloatField(label='Variable 3.7', required=False)
    var73_8 = forms.FloatField(label='Variable 3.8', required=False)
    var73_9 = forms.FloatField(label='Variable 3.9', required=False)
    var73_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var74_1 = forms.FloatField(label='Variable 4.1', required=False)
    var74_2 = forms.FloatField(label='Variable 4.2', required=False)
    var74_3 = forms.FloatField(label='Variable 4.3', required=False)
    var74_4 = forms.FloatField(label='Variable 4.4', required=False)
    var74_5 = forms.FloatField(label='Variable 4.5', required=False)
    var74_6 = forms.FloatField(label='Variable 4.6', required=False)
    var74_7 = forms.FloatField(label='Variable 4.7', required=False)
    var74_8 = forms.FloatField(label='Variable 4.8', required=False)
    var74_9 = forms.FloatField(label='Variable 4.9', required=False)
    var74_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var75_1 = forms.FloatField(label='Variable 5.1', required=False)
    var75_2 = forms.FloatField(label='Variable 5.2', required=False)
    var75_3 = forms.FloatField(label='Variable 5.3', required=False)
    var75_4 = forms.FloatField(label='Variable 5.4', required=False)
    var75_5 = forms.FloatField(label='Variable 5.5', required=False)
    var75_6 = forms.FloatField(label='Variable 5.6', required=False)
    var75_7 = forms.FloatField(label='Variable 5.7', required=False)
    var75_8 = forms.FloatField(label='Variable 5.8', required=False)
    var75_9 = forms.FloatField(label='Variable 5.9', required=False)
    var75_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var76_1 = forms.FloatField(label='Variable 6.1', required=False)
    var76_2 = forms.FloatField(label='Variable 6.2', required=False)
    var76_3 = forms.FloatField(label='Variable 6.3', required=False)
    var76_4 = forms.FloatField(label='Variable 6.4', required=False)
    var76_5 = forms.FloatField(label='Variable 6.5', required=False)
    var76_6 = forms.FloatField(label='Variable 6.6', required=False)
    var76_7 = forms.FloatField(label='Variable 6.7', required=False)
    var76_8 = forms.FloatField(label='Variable 6.8', required=False)
    var76_9 = forms.FloatField(label='Variable 6.9', required=False)
    var76_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var77_1 = forms.FloatField(label='Variable 7.1', required=False)
    var77_2 = forms.FloatField(label='Variable 7.2', required=False)
    var77_3 = forms.FloatField(label='Variable 7.3', required=False)
    var77_4 = forms.FloatField(label='Variable 7.4', required=False)
    var77_5 = forms.FloatField(label='Variable 7.5', required=False)
    var77_6 = forms.FloatField(label='Variable 7.6', required=False)
    var77_7 = forms.FloatField(label='Variable 7.7', required=False)
    var77_8 = forms.FloatField(label='Variable 7.8', required=False)
    var77_9 = forms.FloatField(label='Variable 7.9', required=False)
    var77_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var78_1 = forms.FloatField(label='Variable 8.1', required=False)
    var78_2 = forms.FloatField(label='Variable 8.2', required=False)
    var78_3 = forms.FloatField(label='Variable 8.3', required=False)
    var78_4 = forms.FloatField(label='Variable 8.4', required=False)
    var78_5 = forms.FloatField(label='Variable 8.5', required=False)
    var78_6 = forms.FloatField(label='Variable 8.6', required=False)
    var78_7 = forms.FloatField(label='Variable 8.7', required=False)
    var78_8 = forms.FloatField(label='Variable 8.8', required=False)
    var78_9 = forms.FloatField(label='Variable 8.9', required=False)
    var78_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var79_1 = forms.FloatField(label='Variable 9.1', required=False)
    var79_2 = forms.FloatField(label='Variable 9.2', required=False)
    var79_3 = forms.FloatField(label='Variable 9.3', required=False)
    var79_4 = forms.FloatField(label='Variable 9.4', required=False)
    var79_5 = forms.FloatField(label='Variable 9.5', required=False)
    var79_6 = forms.FloatField(label='Variable 9.6', required=False)
    var79_7 = forms.FloatField(label='Variable 9.7', required=False)
    var79_8 = forms.FloatField(label='Variable 9.8', required=False)
    var79_9 = forms.FloatField(label='Variable 9.9', required=False)
    var79_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var80_1 = forms.FloatField(label='Variable 10.1', required=False)
    var80_2 = forms.FloatField(label='Variable 10.2', required=False)
    var80_3 = forms.FloatField(label='Variable 10.3', required=False)
    var80_4 = forms.FloatField(label='Variable 10.4', required=False)
    var80_5 = forms.FloatField(label='Variable 10.5', required=False)
    var80_6 = forms.FloatField(label='Variable 10.6', required=False)
    var80_7 = forms.FloatField(label='Variable 10.7', required=False)
    var80_8 = forms.FloatField(label='Variable 10.8', required=False)
    var80_9 = forms.FloatField(label='Variable 10.9', required=False)
    var80_10 = forms.FloatField(label='Variable 10.10', required=False)

    var81_1 = forms.FloatField(label='Variable 1.1', required=False)
    var81_2 = forms.FloatField(label='Variable 1.2', required=False)
    var81_3 = forms.FloatField(label='Variable 1.3', required=False)
    var81_4 = forms.FloatField(label='Variable 1.4', required=False)
    var81_5 = forms.FloatField(label='Variable 1.5', required=False)
    var81_6 = forms.FloatField(label='Variable 1.6', required=False)
    var81_7 = forms.FloatField(label='Variable 1.7', required=False)
    var81_8 = forms.FloatField(label='Variable 1.8', required=False)
    var81_9 = forms.FloatField(label='Variable 1.9', required=False)
    var81_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var82_1 = forms.FloatField(label='Variable 2.1', required=False)
    var82_2 = forms.FloatField(label='Variable 2.2', required=False)
    var82_3 = forms.FloatField(label='Variable 2.3', required=False)
    var82_4 = forms.FloatField(label='Variable 2.4', required=False)
    var82_5 = forms.FloatField(label='Variable 2.5', required=False)
    var82_6 = forms.FloatField(label='Variable 2.6', required=False)
    var82_7 = forms.FloatField(label='Variable 2.7', required=False)
    var82_8 = forms.FloatField(label='Variable 2.8', required=False)
    var82_9 = forms.FloatField(label='Variable 2.9', required=False)
    var82_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var83_1 = forms.FloatField(label='Variable 3.1', required=False)
    var83_2 = forms.FloatField(label='Variable 3.2', required=False)
    var83_3 = forms.FloatField(label='Variable 3.3', required=False)
    var83_4 = forms.FloatField(label='Variable 3.4', required=False)
    var83_5 = forms.FloatField(label='Variable 3.5', required=False)
    var83_6 = forms.FloatField(label='Variable 3.6', required=False)
    var83_7 = forms.FloatField(label='Variable 3.7', required=False)
    var83_8 = forms.FloatField(label='Variable 3.8', required=False)
    var83_9 = forms.FloatField(label='Variable 3.9', required=False)
    var83_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var84_1 = forms.FloatField(label='Variable 4.1', required=False)
    var84_2 = forms.FloatField(label='Variable 4.2', required=False)
    var84_3 = forms.FloatField(label='Variable 4.3', required=False)
    var84_4 = forms.FloatField(label='Variable 4.4', required=False)
    var84_5 = forms.FloatField(label='Variable 4.5', required=False)
    var84_6 = forms.FloatField(label='Variable 4.6', required=False)
    var84_7 = forms.FloatField(label='Variable 4.7', required=False)
    var84_8 = forms.FloatField(label='Variable 4.8', required=False)
    var84_9 = forms.FloatField(label='Variable 4.9', required=False)
    var84_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var85_1 = forms.FloatField(label='Variable 5.1', required=False)
    var85_2 = forms.FloatField(label='Variable 5.2', required=False)
    var85_3 = forms.FloatField(label='Variable 5.3', required=False)
    var85_4 = forms.FloatField(label='Variable 5.4', required=False)
    var85_5 = forms.FloatField(label='Variable 5.5', required=False)
    var85_6 = forms.FloatField(label='Variable 5.6', required=False)
    var85_7 = forms.FloatField(label='Variable 5.7', required=False)
    var85_8 = forms.FloatField(label='Variable 5.8', required=False)
    var85_9 = forms.FloatField(label='Variable 5.9', required=False)
    var85_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var86_1 = forms.FloatField(label='Variable 6.1', required=False)
    var86_2 = forms.FloatField(label='Variable 6.2', required=False)
    var86_3 = forms.FloatField(label='Variable 6.3', required=False)
    var86_4 = forms.FloatField(label='Variable 6.4', required=False)
    var86_5 = forms.FloatField(label='Variable 6.5', required=False)
    var86_6 = forms.FloatField(label='Variable 6.6', required=False)
    var86_7 = forms.FloatField(label='Variable 6.7', required=False)
    var86_8 = forms.FloatField(label='Variable 6.8', required=False)
    var86_9 = forms.FloatField(label='Variable 6.9', required=False)
    var86_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var87_1 = forms.FloatField(label='Variable 7.1', required=False)
    var87_2 = forms.FloatField(label='Variable 7.2', required=False)
    var87_3 = forms.FloatField(label='Variable 7.3', required=False)
    var87_4 = forms.FloatField(label='Variable 7.4', required=False)
    var87_5 = forms.FloatField(label='Variable 7.5', required=False)
    var87_6 = forms.FloatField(label='Variable 7.6', required=False)
    var87_7 = forms.FloatField(label='Variable 7.7', required=False)
    var87_8 = forms.FloatField(label='Variable 7.8', required=False)
    var87_9 = forms.FloatField(label='Variable 7.9', required=False)
    var87_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var88_1 = forms.FloatField(label='Variable 8.1', required=False)
    var88_2 = forms.FloatField(label='Variable 8.2', required=False)
    var88_3 = forms.FloatField(label='Variable 8.3', required=False)
    var88_4 = forms.FloatField(label='Variable 8.4', required=False)
    var88_5 = forms.FloatField(label='Variable 8.5', required=False)
    var88_6 = forms.FloatField(label='Variable 8.6', required=False)
    var88_7 = forms.FloatField(label='Variable 8.7', required=False)
    var88_8 = forms.FloatField(label='Variable 8.8', required=False)
    var88_9 = forms.FloatField(label='Variable 8.9', required=False)
    var88_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var89_1 = forms.FloatField(label='Variable 9.1', required=False)
    var89_2 = forms.FloatField(label='Variable 9.2', required=False)
    var89_3 = forms.FloatField(label='Variable 9.3', required=False)
    var89_4 = forms.FloatField(label='Variable 9.4', required=False)
    var89_5 = forms.FloatField(label='Variable 9.5', required=False)
    var89_6 = forms.FloatField(label='Variable 9.6', required=False)
    var89_7 = forms.FloatField(label='Variable 9.7', required=False)
    var89_8 = forms.FloatField(label='Variable 9.8', required=False)
    var89_9 = forms.FloatField(label='Variable 9.9', required=False)
    var89_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var90_1 = forms.FloatField(label='Variable 10.1', required=False)
    var90_2 = forms.FloatField(label='Variable 10.2', required=False)
    var90_3 = forms.FloatField(label='Variable 10.3', required=False)
    var90_4 = forms.FloatField(label='Variable 10.4', required=False)
    var90_5 = forms.FloatField(label='Variable 10.5', required=False)
    var90_6 = forms.FloatField(label='Variable 10.6', required=False)
    var90_7 = forms.FloatField(label='Variable 10.7', required=False)
    var90_8 = forms.FloatField(label='Variable 10.8', required=False)
    var90_9 = forms.FloatField(label='Variable 10.9', required=False)
    var90_10 = forms.FloatField(label='Variable 10.10', required=False)


    var91_1 = forms.FloatField(label='Variable 1.1', required=False)
    var91_2 = forms.FloatField(label='Variable 1.2', required=False)
    var91_3 = forms.FloatField(label='Variable 1.3', required=False)
    var91_4 = forms.FloatField(label='Variable 1.4', required=False)
    var91_5 = forms.FloatField(label='Variable 1.5', required=False)
    var91_6 = forms.FloatField(label='Variable 1.6', required=False)
    var91_7 = forms.FloatField(label='Variable 1.7', required=False)
    var91_8 = forms.FloatField(label='Variable 1.8', required=False)
    var91_9 = forms.FloatField(label='Variable 1.9', required=False)
    var91_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var92_1 = forms.FloatField(label='Variable 2.1', required=False)
    var92_2 = forms.FloatField(label='Variable 2.2', required=False)
    var92_3 = forms.FloatField(label='Variable 2.3', required=False)
    var92_4 = forms.FloatField(label='Variable 2.4', required=False)
    var92_5 = forms.FloatField(label='Variable 2.5', required=False)
    var92_6 = forms.FloatField(label='Variable 2.6', required=False)
    var92_7 = forms.FloatField(label='Variable 2.7', required=False)
    var92_8 = forms.FloatField(label='Variable 2.8', required=False)
    var92_9 = forms.FloatField(label='Variable 2.9', required=False)
    var92_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var93_1 = forms.FloatField(label='Variable 3.1', required=False)
    var93_2 = forms.FloatField(label='Variable 3.2', required=False)
    var93_3 = forms.FloatField(label='Variable 3.3', required=False)
    var93_4 = forms.FloatField(label='Variable 3.4', required=False)
    var93_5 = forms.FloatField(label='Variable 3.5', required=False)
    var93_6 = forms.FloatField(label='Variable 3.6', required=False)
    var93_7 = forms.FloatField(label='Variable 3.7', required=False)
    var93_8 = forms.FloatField(label='Variable 3.8', required=False)
    var93_9 = forms.FloatField(label='Variable 3.9', required=False)
    var93_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var94_1 = forms.FloatField(label='Variable 4.1', required=False)
    var94_2 = forms.FloatField(label='Variable 4.2', required=False)
    var94_3 = forms.FloatField(label='Variable 4.3', required=False)
    var94_4 = forms.FloatField(label='Variable 4.4', required=False)
    var94_5 = forms.FloatField(label='Variable 4.5', required=False)
    var94_6 = forms.FloatField(label='Variable 4.6', required=False)
    var94_7 = forms.FloatField(label='Variable 4.7', required=False)
    var94_8 = forms.FloatField(label='Variable 4.8', required=False)
    var94_9 = forms.FloatField(label='Variable 4.9', required=False)
    var94_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var95_1 = forms.FloatField(label='Variable 5.1', required=False)
    var95_2 = forms.FloatField(label='Variable 5.2', required=False)
    var95_3 = forms.FloatField(label='Variable 5.3', required=False)
    var95_4 = forms.FloatField(label='Variable 5.4', required=False)
    var95_5 = forms.FloatField(label='Variable 5.5', required=False)
    var95_6 = forms.FloatField(label='Variable 5.6', required=False)
    var95_7 = forms.FloatField(label='Variable 5.7', required=False)
    var95_8 = forms.FloatField(label='Variable 5.8', required=False)
    var95_9 = forms.FloatField(label='Variable 5.9', required=False)
    var95_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var96_1 = forms.FloatField(label='Variable 6.1', required=False)
    var96_2 = forms.FloatField(label='Variable 6.2', required=False)
    var96_3 = forms.FloatField(label='Variable 6.3', required=False)
    var96_4 = forms.FloatField(label='Variable 6.4', required=False)
    var96_5 = forms.FloatField(label='Variable 6.5', required=False)
    var96_6 = forms.FloatField(label='Variable 6.6', required=False)
    var96_7 = forms.FloatField(label='Variable 6.7', required=False)
    var96_8 = forms.FloatField(label='Variable 6.8', required=False)
    var96_9 = forms.FloatField(label='Variable 6.9', required=False)
    var96_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var97_1 = forms.FloatField(label='Variable 7.1', required=False)
    var97_2 = forms.FloatField(label='Variable 7.2', required=False)
    var97_3 = forms.FloatField(label='Variable 7.3', required=False)
    var97_4 = forms.FloatField(label='Variable 7.4', required=False)
    var97_5 = forms.FloatField(label='Variable 7.5', required=False)
    var97_6 = forms.FloatField(label='Variable 7.6', required=False)
    var97_7 = forms.FloatField(label='Variable 7.7', required=False)
    var97_8 = forms.FloatField(label='Variable 7.8', required=False)
    var97_9 = forms.FloatField(label='Variable 7.9', required=False)
    var97_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var98_1 = forms.FloatField(label='Variable 8.1', required=False)
    var98_2 = forms.FloatField(label='Variable 8.2', required=False)
    var98_3 = forms.FloatField(label='Variable 8.3', required=False)
    var98_4 = forms.FloatField(label='Variable 8.4', required=False)
    var98_5 = forms.FloatField(label='Variable 8.5', required=False)
    var98_6 = forms.FloatField(label='Variable 8.6', required=False)
    var98_7 = forms.FloatField(label='Variable 8.7', required=False)
    var98_8 = forms.FloatField(label='Variable 8.8', required=False)
    var98_9 = forms.FloatField(label='Variable 8.9', required=False)
    var98_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var99_1 = forms.FloatField(label='Variable 9.1', required=False)
    var99_2 = forms.FloatField(label='Variable 9.2', required=False)
    var99_3 = forms.FloatField(label='Variable 9.3', required=False)
    var99_4 = forms.FloatField(label='Variable 9.4', required=False)
    var99_5 = forms.FloatField(label='Variable 9.5', required=False)
    var99_6 = forms.FloatField(label='Variable 9.6', required=False)
    var99_7 = forms.FloatField(label='Variable 9.7', required=False)
    var99_8 = forms.FloatField(label='Variable 9.8', required=False)
    var99_9 = forms.FloatField(label='Variable 9.9', required=False)
    var99_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var100_1 = forms.FloatField(label='Variable 10.1', required=False)
    var100_2 = forms.FloatField(label='Variable 10.2', required=False)
    var100_3 = forms.FloatField(label='Variable 10.3', required=False)
    var100_4 = forms.FloatField(label='Variable 10.4', required=False)
    var100_5 = forms.FloatField(label='Variable 10.5', required=False)
    var100_6 = forms.FloatField(label='Variable 10.6', required=False)
    var100_7 = forms.FloatField(label='Variable 10.7', required=False)
    var100_8 = forms.FloatField(label='Variable 10.8', required=False)
    var100_9 = forms.FloatField(label='Variable 10.9', required=False)
    var100_10 = forms.FloatField(label='Variable 10.10', required=False)

    var101_1 = forms.FloatField(label='Variable 1.1', required=False)
    var101_2 = forms.FloatField(label='Variable 1.2', required=False)
    var101_3 = forms.FloatField(label='Variable 1.3', required=False)
    var101_4 = forms.FloatField(label='Variable 1.4', required=False)
    var101_5 = forms.FloatField(label='Variable 1.5', required=False)
    var101_6 = forms.FloatField(label='Variable 1.6', required=False)
    var101_7 = forms.FloatField(label='Variable 1.7', required=False)
    var101_8 = forms.FloatField(label='Variable 1.8', required=False)
    var101_9 = forms.FloatField(label='Variable 1.9', required=False)
    var101_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var102_1 = forms.FloatField(label='Variable 2.1', required=False)
    var102_2 = forms.FloatField(label='Variable 2.2', required=False)
    var102_3 = forms.FloatField(label='Variable 2.3', required=False)
    var102_4 = forms.FloatField(label='Variable 2.4', required=False)
    var102_5 = forms.FloatField(label='Variable 2.5', required=False)
    var102_6 = forms.FloatField(label='Variable 2.6', required=False)
    var102_7 = forms.FloatField(label='Variable 2.7', required=False)
    var102_8 = forms.FloatField(label='Variable 2.8', required=False)
    var102_9 = forms.FloatField(label='Variable 2.9', required=False)
    var102_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var103_1 = forms.FloatField(label='Variable 3.1', required=False)
    var103_2 = forms.FloatField(label='Variable 3.2', required=False)
    var103_3 = forms.FloatField(label='Variable 3.3', required=False)
    var103_4 = forms.FloatField(label='Variable 3.4', required=False)
    var103_5 = forms.FloatField(label='Variable 3.5', required=False)
    var103_6 = forms.FloatField(label='Variable 3.6', required=False)
    var103_7 = forms.FloatField(label='Variable 3.7', required=False)
    var103_8 = forms.FloatField(label='Variable 3.8', required=False)
    var103_9 = forms.FloatField(label='Variable 3.9', required=False)
    var103_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var104_1 = forms.FloatField(label='Variable 4.1', required=False)
    var104_2 = forms.FloatField(label='Variable 4.2', required=False)
    var104_3 = forms.FloatField(label='Variable 4.3', required=False)
    var104_4 = forms.FloatField(label='Variable 4.4', required=False)
    var104_5 = forms.FloatField(label='Variable 4.5', required=False)
    var104_6 = forms.FloatField(label='Variable 4.6', required=False)
    var104_7 = forms.FloatField(label='Variable 4.7', required=False)
    var104_8 = forms.FloatField(label='Variable 4.8', required=False)
    var104_9 = forms.FloatField(label='Variable 4.9', required=False)
    var104_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var105_1 = forms.FloatField(label='Variable 5.1', required=False)
    var105_2 = forms.FloatField(label='Variable 5.2', required=False)
    var105_3 = forms.FloatField(label='Variable 5.3', required=False)
    var105_4 = forms.FloatField(label='Variable 5.4', required=False)
    var105_5 = forms.FloatField(label='Variable 5.5', required=False)
    var105_6 = forms.FloatField(label='Variable 5.6', required=False)
    var105_7 = forms.FloatField(label='Variable 5.7', required=False)
    var105_8 = forms.FloatField(label='Variable 5.8', required=False)
    var105_9 = forms.FloatField(label='Variable 5.9', required=False)
    var105_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var106_1 = forms.FloatField(label='Variable 6.1', required=False)
    var106_2 = forms.FloatField(label='Variable 6.2', required=False)
    var106_3 = forms.FloatField(label='Variable 6.3', required=False)
    var106_4 = forms.FloatField(label='Variable 6.4', required=False)
    var106_5 = forms.FloatField(label='Variable 6.5', required=False)
    var106_6 = forms.FloatField(label='Variable 6.6', required=False)
    var106_7 = forms.FloatField(label='Variable 6.7', required=False)
    var106_8 = forms.FloatField(label='Variable 6.8', required=False)
    var106_9 = forms.FloatField(label='Variable 6.9', required=False)
    var106_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var107_1 = forms.FloatField(label='Variable 7.1', required=False)
    var107_2 = forms.FloatField(label='Variable 7.2', required=False)
    var107_3 = forms.FloatField(label='Variable 7.3', required=False)
    var107_4 = forms.FloatField(label='Variable 7.4', required=False)
    var107_5 = forms.FloatField(label='Variable 7.5', required=False)
    var107_6 = forms.FloatField(label='Variable 7.6', required=False)
    var107_7 = forms.FloatField(label='Variable 7.7', required=False)
    var107_8 = forms.FloatField(label='Variable 7.8', required=False)
    var107_9 = forms.FloatField(label='Variable 7.9', required=False)
    var107_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var108_1 = forms.FloatField(label='Variable 8.1', required=False)
    var108_2 = forms.FloatField(label='Variable 8.2', required=False)
    var108_3 = forms.FloatField(label='Variable 8.3', required=False)
    var108_4 = forms.FloatField(label='Variable 8.4', required=False)
    var108_5 = forms.FloatField(label='Variable 8.5', required=False)
    var108_6 = forms.FloatField(label='Variable 8.6', required=False)
    var108_7 = forms.FloatField(label='Variable 8.7', required=False)
    var108_8 = forms.FloatField(label='Variable 8.8', required=False)
    var108_9 = forms.FloatField(label='Variable 8.9', required=False)
    var108_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var109_1 = forms.FloatField(label='Variable 9.1', required=False)
    var109_2 = forms.FloatField(label='Variable 9.2', required=False)
    var109_3 = forms.FloatField(label='Variable 9.3', required=False)
    var109_4 = forms.FloatField(label='Variable 9.4', required=False)
    var109_5 = forms.FloatField(label='Variable 9.5', required=False)
    var109_6 = forms.FloatField(label='Variable 9.6', required=False)
    var109_7 = forms.FloatField(label='Variable 9.7', required=False)
    var109_8 = forms.FloatField(label='Variable 9.8', required=False)
    var109_9 = forms.FloatField(label='Variable 9.9', required=False)
    var109_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var110_1 = forms.FloatField(label='Variable 10.1', required=False)
    var110_2 = forms.FloatField(label='Variable 10.2', required=False)
    var110_3 = forms.FloatField(label='Variable 10.3', required=False)
    var110_4 = forms.FloatField(label='Variable 10.4', required=False)
    var110_5 = forms.FloatField(label='Variable 10.5', required=False)
    var110_6 = forms.FloatField(label='Variable 10.6', required=False)
    var110_7 = forms.FloatField(label='Variable 10.7', required=False)
    var110_8 = forms.FloatField(label='Variable 10.8', required=False)
    var110_9 = forms.FloatField(label='Variable 10.9', required=False)
    var110_10 = forms.FloatField(label='Variable 10.10', required=False)

    var111_1 = forms.FloatField(label='Variable 1.1', required=False)
    var111_2 = forms.FloatField(label='Variable 1.2', required=False)
    var111_3 = forms.FloatField(label='Variable 1.3', required=False)
    var111_4 = forms.FloatField(label='Variable 1.4', required=False)
    var111_5 = forms.FloatField(label='Variable 1.5', required=False)
    var111_6 = forms.FloatField(label='Variable 1.6', required=False)
    var111_7 = forms.FloatField(label='Variable 1.7', required=False)
    var111_8 = forms.FloatField(label='Variable 1.8', required=False)
    var111_9 = forms.FloatField(label='Variable 1.9', required=False)
    var111_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var112_1 = forms.FloatField(label='Variable 2.1', required=False)
    var112_2 = forms.FloatField(label='Variable 2.2', required=False)
    var112_3 = forms.FloatField(label='Variable 2.3', required=False)
    var112_4 = forms.FloatField(label='Variable 2.4', required=False)
    var112_5 = forms.FloatField(label='Variable 2.5', required=False)
    var112_6 = forms.FloatField(label='Variable 2.6', required=False)
    var112_7 = forms.FloatField(label='Variable 2.7', required=False)
    var112_8 = forms.FloatField(label='Variable 2.8', required=False)
    var112_9 = forms.FloatField(label='Variable 2.9', required=False)
    var112_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var113_1 = forms.FloatField(label='Variable 3.1', required=False)
    var113_2 = forms.FloatField(label='Variable 3.2', required=False)
    var113_3 = forms.FloatField(label='Variable 3.3', required=False)
    var113_4 = forms.FloatField(label='Variable 3.4', required=False)
    var113_5 = forms.FloatField(label='Variable 3.5', required=False)
    var113_6 = forms.FloatField(label='Variable 3.6', required=False)
    var113_7 = forms.FloatField(label='Variable 3.7', required=False)
    var113_8 = forms.FloatField(label='Variable 3.8', required=False)
    var113_9 = forms.FloatField(label='Variable 3.9', required=False)
    var113_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var114_1 = forms.FloatField(label='Variable 4.1', required=False)
    var114_2 = forms.FloatField(label='Variable 4.2', required=False)
    var114_3 = forms.FloatField(label='Variable 4.3', required=False)
    var114_4 = forms.FloatField(label='Variable 4.4', required=False)
    var114_5 = forms.FloatField(label='Variable 4.5', required=False)
    var114_6 = forms.FloatField(label='Variable 4.6', required=False)
    var114_7 = forms.FloatField(label='Variable 4.7', required=False)
    var114_8 = forms.FloatField(label='Variable 4.8', required=False)
    var114_9 = forms.FloatField(label='Variable 4.9', required=False)
    var114_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var115_1 = forms.FloatField(label='Variable 5.1', required=False)
    var115_2 = forms.FloatField(label='Variable 5.2', required=False)
    var115_3 = forms.FloatField(label='Variable 5.3', required=False)
    var115_4 = forms.FloatField(label='Variable 5.4', required=False)
    var115_5 = forms.FloatField(label='Variable 5.5', required=False)
    var115_6 = forms.FloatField(label='Variable 5.6', required=False)
    var115_7 = forms.FloatField(label='Variable 5.7', required=False)
    var115_8 = forms.FloatField(label='Variable 5.8', required=False)
    var115_9 = forms.FloatField(label='Variable 5.9', required=False)
    var115_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var116_1 = forms.FloatField(label='Variable 6.1', required=False)
    var116_2 = forms.FloatField(label='Variable 6.2', required=False)
    var116_3 = forms.FloatField(label='Variable 6.3', required=False)
    var116_4 = forms.FloatField(label='Variable 6.4', required=False)
    var116_5 = forms.FloatField(label='Variable 6.5', required=False)
    var116_6 = forms.FloatField(label='Variable 6.6', required=False)
    var116_7 = forms.FloatField(label='Variable 6.7', required=False)
    var116_8 = forms.FloatField(label='Variable 6.8', required=False)
    var116_9 = forms.FloatField(label='Variable 6.9', required=False)
    var116_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var117_1 = forms.FloatField(label='Variable 7.1', required=False)
    var117_2 = forms.FloatField(label='Variable 7.2', required=False)
    var117_3 = forms.FloatField(label='Variable 7.3', required=False)
    var117_4 = forms.FloatField(label='Variable 7.4', required=False)
    var117_5 = forms.FloatField(label='Variable 7.5', required=False)
    var117_6 = forms.FloatField(label='Variable 7.6', required=False)
    var117_7 = forms.FloatField(label='Variable 7.7', required=False)
    var117_8 = forms.FloatField(label='Variable 7.8', required=False)
    var117_9 = forms.FloatField(label='Variable 7.9', required=False)
    var117_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var118_1 = forms.FloatField(label='Variable 8.1', required=False)
    var118_2 = forms.FloatField(label='Variable 8.2', required=False)
    var118_3 = forms.FloatField(label='Variable 8.3', required=False)
    var118_4 = forms.FloatField(label='Variable 8.4', required=False)
    var118_5 = forms.FloatField(label='Variable 8.5', required=False)
    var118_6 = forms.FloatField(label='Variable 8.6', required=False)
    var118_7 = forms.FloatField(label='Variable 8.7', required=False)
    var118_8 = forms.FloatField(label='Variable 8.8', required=False)
    var118_9 = forms.FloatField(label='Variable 8.9', required=False)
    var118_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var119_1 = forms.FloatField(label='Variable 9.1', required=False)
    var119_2 = forms.FloatField(label='Variable 9.2', required=False)
    var119_3 = forms.FloatField(label='Variable 9.3', required=False)
    var119_4 = forms.FloatField(label='Variable 9.4', required=False)
    var119_5 = forms.FloatField(label='Variable 9.5', required=False)
    var119_6 = forms.FloatField(label='Variable 9.6', required=False)
    var119_7 = forms.FloatField(label='Variable 9.7', required=False)
    var119_8 = forms.FloatField(label='Variable 9.8', required=False)
    var119_9 = forms.FloatField(label='Variable 9.9', required=False)
    var119_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var120_1 = forms.FloatField(label='Variable 10.1', required=False)
    var120_2 = forms.FloatField(label='Variable 10.2', required=False)
    var120_3 = forms.FloatField(label='Variable 10.3', required=False)
    var120_4 = forms.FloatField(label='Variable 10.4', required=False)
    var120_5 = forms.FloatField(label='Variable 10.5', required=False)
    var120_6 = forms.FloatField(label='Variable 10.6', required=False)
    var120_7 = forms.FloatField(label='Variable 10.7', required=False)
    var120_8 = forms.FloatField(label='Variable 10.8', required=False)
    var120_9 = forms.FloatField(label='Variable 10.9', required=False)
    var120_10 = forms.FloatField(label='Variable 10.10', required=False)

    var121_1 = forms.FloatField(label='Variable 1.1', required=False)
    var121_2 = forms.FloatField(label='Variable 1.2', required=False)
    var121_3 = forms.FloatField(label='Variable 1.3', required=False)
    var121_4 = forms.FloatField(label='Variable 1.4', required=False)
    var121_5 = forms.FloatField(label='Variable 1.5', required=False)
    var121_6 = forms.FloatField(label='Variable 1.6', required=False)
    var121_7 = forms.FloatField(label='Variable 1.7', required=False)
    var121_8 = forms.FloatField(label='Variable 1.8', required=False)
    var121_9 = forms.FloatField(label='Variable 1.9', required=False)
    var121_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var122_1 = forms.FloatField(label='Variable 2.1', required=False)
    var122_2 = forms.FloatField(label='Variable 2.2', required=False)
    var122_3 = forms.FloatField(label='Variable 2.3', required=False)
    var122_4 = forms.FloatField(label='Variable 2.4', required=False)
    var122_5 = forms.FloatField(label='Variable 2.5', required=False)
    var122_6 = forms.FloatField(label='Variable 2.6', required=False)
    var122_7 = forms.FloatField(label='Variable 2.7', required=False)
    var122_8 = forms.FloatField(label='Variable 2.8', required=False)
    var122_9 = forms.FloatField(label='Variable 2.9', required=False)
    var122_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var123_1 = forms.FloatField(label='Variable 3.1', required=False)
    var123_2 = forms.FloatField(label='Variable 3.2', required=False)
    var123_3 = forms.FloatField(label='Variable 3.3', required=False)
    var123_4 = forms.FloatField(label='Variable 3.4', required=False)
    var123_5 = forms.FloatField(label='Variable 3.5', required=False)
    var123_6 = forms.FloatField(label='Variable 3.6', required=False)
    var123_7 = forms.FloatField(label='Variable 3.7', required=False)
    var123_8 = forms.FloatField(label='Variable 3.8', required=False)
    var123_9 = forms.FloatField(label='Variable 3.9', required=False)
    var123_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var124_1 = forms.FloatField(label='Variable 4.1', required=False)
    var124_2 = forms.FloatField(label='Variable 4.2', required=False)
    var124_3 = forms.FloatField(label='Variable 4.3', required=False)
    var124_4 = forms.FloatField(label='Variable 4.4', required=False)
    var124_5 = forms.FloatField(label='Variable 4.5', required=False)
    var124_6 = forms.FloatField(label='Variable 4.6', required=False)
    var124_7 = forms.FloatField(label='Variable 4.7', required=False)
    var124_8 = forms.FloatField(label='Variable 4.8', required=False)
    var124_9 = forms.FloatField(label='Variable 4.9', required=False)
    var124_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var125_1 = forms.FloatField(label='Variable 5.1', required=False)
    var125_2 = forms.FloatField(label='Variable 5.2', required=False)
    var125_3 = forms.FloatField(label='Variable 5.3', required=False)
    var125_4 = forms.FloatField(label='Variable 5.4', required=False)
    var125_5 = forms.FloatField(label='Variable 5.5', required=False)
    var125_6 = forms.FloatField(label='Variable 5.6', required=False)
    var125_7 = forms.FloatField(label='Variable 5.7', required=False)
    var125_8 = forms.FloatField(label='Variable 5.8', required=False)
    var125_9 = forms.FloatField(label='Variable 5.9', required=False)
    var125_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var126_1 = forms.FloatField(label='Variable 6.1', required=False)
    var126_2 = forms.FloatField(label='Variable 6.2', required=False)
    var126_3 = forms.FloatField(label='Variable 6.3', required=False)
    var126_4 = forms.FloatField(label='Variable 6.4', required=False)
    var126_5 = forms.FloatField(label='Variable 6.5', required=False)
    var126_6 = forms.FloatField(label='Variable 6.6', required=False)
    var126_7 = forms.FloatField(label='Variable 6.7', required=False)
    var126_8 = forms.FloatField(label='Variable 6.8', required=False)
    var126_9 = forms.FloatField(label='Variable 6.9', required=False)
    var126_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var127_1 = forms.FloatField(label='Variable 7.1', required=False)
    var127_2 = forms.FloatField(label='Variable 7.2', required=False)
    var127_3 = forms.FloatField(label='Variable 7.3', required=False)
    var127_4 = forms.FloatField(label='Variable 7.4', required=False)
    var127_5 = forms.FloatField(label='Variable 7.5', required=False)
    var127_6 = forms.FloatField(label='Variable 7.6', required=False)
    var127_7 = forms.FloatField(label='Variable 7.7', required=False)
    var127_8 = forms.FloatField(label='Variable 7.8', required=False)
    var127_9 = forms.FloatField(label='Variable 7.9', required=False)
    var127_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var128_1 = forms.FloatField(label='Variable 8.1', required=False)
    var128_2 = forms.FloatField(label='Variable 8.2', required=False)
    var128_3 = forms.FloatField(label='Variable 8.3', required=False)
    var128_4 = forms.FloatField(label='Variable 8.4', required=False)
    var128_5 = forms.FloatField(label='Variable 8.5', required=False)
    var128_6 = forms.FloatField(label='Variable 8.6', required=False)
    var128_7 = forms.FloatField(label='Variable 8.7', required=False)
    var128_8 = forms.FloatField(label='Variable 8.8', required=False)
    var128_9 = forms.FloatField(label='Variable 8.9', required=False)
    var128_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var129_1 = forms.FloatField(label='Variable 9.1', required=False)
    var129_2 = forms.FloatField(label='Variable 9.2', required=False)
    var129_3 = forms.FloatField(label='Variable 9.3', required=False)
    var129_4 = forms.FloatField(label='Variable 9.4', required=False)
    var129_5 = forms.FloatField(label='Variable 9.5', required=False)
    var129_6 = forms.FloatField(label='Variable 9.6', required=False)
    var129_7 = forms.FloatField(label='Variable 9.7', required=False)
    var129_8 = forms.FloatField(label='Variable 9.8', required=False)
    var129_9 = forms.FloatField(label='Variable 9.9', required=False)
    var129_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var130_1 = forms.FloatField(label='Variable 10.1', required=False)
    var130_2 = forms.FloatField(label='Variable 10.2', required=False)
    var130_3 = forms.FloatField(label='Variable 10.3', required=False)
    var130_4 = forms.FloatField(label='Variable 10.4', required=False)
    var130_5 = forms.FloatField(label='Variable 10.5', required=False)
    var130_6 = forms.FloatField(label='Variable 10.6', required=False)
    var130_7 = forms.FloatField(label='Variable 10.7', required=False)
    var130_8 = forms.FloatField(label='Variable 10.8', required=False)
    var130_9 = forms.FloatField(label='Variable 10.9', required=False)
    var130_10 = forms.FloatField(label='Variable 10.10', required=False)

    var131_1 = forms.FloatField(label='Variable 1.1', required=False)
    var131_2 = forms.FloatField(label='Variable 1.2', required=False)
    var131_3 = forms.FloatField(label='Variable 1.3', required=False)
    var131_4 = forms.FloatField(label='Variable 1.4', required=False)
    var131_5 = forms.FloatField(label='Variable 1.5', required=False)
    var131_6 = forms.FloatField(label='Variable 1.6', required=False)
    var131_7 = forms.FloatField(label='Variable 1.7', required=False)
    var131_8 = forms.FloatField(label='Variable 1.8', required=False)
    var131_9 = forms.FloatField(label='Variable 1.9', required=False)
    var131_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var132_1 = forms.FloatField(label='Variable 2.1', required=False)
    var132_2 = forms.FloatField(label='Variable 2.2', required=False)
    var132_3 = forms.FloatField(label='Variable 2.3', required=False)
    var132_4 = forms.FloatField(label='Variable 2.4', required=False)
    var132_5 = forms.FloatField(label='Variable 2.5', required=False)
    var132_6 = forms.FloatField(label='Variable 2.6', required=False)
    var132_7 = forms.FloatField(label='Variable 2.7', required=False)
    var132_8 = forms.FloatField(label='Variable 2.8', required=False)
    var132_9 = forms.FloatField(label='Variable 2.9', required=False)
    var132_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var133_1 = forms.FloatField(label='Variable 3.1', required=False)
    var133_2 = forms.FloatField(label='Variable 3.2', required=False)
    var133_3 = forms.FloatField(label='Variable 3.3', required=False)
    var133_4 = forms.FloatField(label='Variable 3.4', required=False)
    var133_5 = forms.FloatField(label='Variable 3.5', required=False)
    var133_6 = forms.FloatField(label='Variable 3.6', required=False)
    var133_7 = forms.FloatField(label='Variable 3.7', required=False)
    var133_8 = forms.FloatField(label='Variable 3.8', required=False)
    var133_9 = forms.FloatField(label='Variable 3.9', required=False)
    var133_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var134_1 = forms.FloatField(label='Variable 4.1', required=False)
    var134_2 = forms.FloatField(label='Variable 4.2', required=False)
    var134_3 = forms.FloatField(label='Variable 4.3', required=False)
    var134_4 = forms.FloatField(label='Variable 4.4', required=False)
    var134_5 = forms.FloatField(label='Variable 4.5', required=False)
    var134_6 = forms.FloatField(label='Variable 4.6', required=False)
    var134_7 = forms.FloatField(label='Variable 4.7', required=False)
    var134_8 = forms.FloatField(label='Variable 4.8', required=False)
    var134_9 = forms.FloatField(label='Variable 4.9', required=False)
    var134_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var135_1 = forms.FloatField(label='Variable 5.1', required=False)
    var135_2 = forms.FloatField(label='Variable 5.2', required=False)
    var135_3 = forms.FloatField(label='Variable 5.3', required=False)
    var135_4 = forms.FloatField(label='Variable 5.4', required=False)
    var135_5 = forms.FloatField(label='Variable 5.5', required=False)
    var135_6 = forms.FloatField(label='Variable 5.6', required=False)
    var135_7 = forms.FloatField(label='Variable 5.7', required=False)
    var135_8 = forms.FloatField(label='Variable 5.8', required=False)
    var135_9 = forms.FloatField(label='Variable 5.9', required=False)
    var135_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var136_1 = forms.FloatField(label='Variable 6.1', required=False)
    var136_2 = forms.FloatField(label='Variable 6.2', required=False)
    var136_3 = forms.FloatField(label='Variable 6.3', required=False)
    var136_4 = forms.FloatField(label='Variable 6.4', required=False)
    var136_5 = forms.FloatField(label='Variable 6.5', required=False)
    var136_6 = forms.FloatField(label='Variable 6.6', required=False)
    var136_7 = forms.FloatField(label='Variable 6.7', required=False)
    var136_8 = forms.FloatField(label='Variable 6.8', required=False)
    var136_9 = forms.FloatField(label='Variable 6.9', required=False)
    var136_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var137_1 = forms.FloatField(label='Variable 7.1', required=False)
    var137_2 = forms.FloatField(label='Variable 7.2', required=False)
    var137_3 = forms.FloatField(label='Variable 7.3', required=False)
    var137_4 = forms.FloatField(label='Variable 7.4', required=False)
    var137_5 = forms.FloatField(label='Variable 7.5', required=False)
    var137_6 = forms.FloatField(label='Variable 7.6', required=False)
    var137_7 = forms.FloatField(label='Variable 7.7', required=False)
    var137_8 = forms.FloatField(label='Variable 7.8', required=False)
    var137_9 = forms.FloatField(label='Variable 7.9', required=False)
    var137_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var138_1 = forms.FloatField(label='Variable 8.1', required=False)
    var138_2 = forms.FloatField(label='Variable 8.2', required=False)
    var138_3 = forms.FloatField(label='Variable 8.3', required=False)
    var138_4 = forms.FloatField(label='Variable 8.4', required=False)
    var138_5 = forms.FloatField(label='Variable 8.5', required=False)
    var138_6 = forms.FloatField(label='Variable 8.6', required=False)
    var138_7 = forms.FloatField(label='Variable 8.7', required=False)
    var138_8 = forms.FloatField(label='Variable 8.8', required=False)
    var138_9 = forms.FloatField(label='Variable 8.9', required=False)
    var138_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var139_1 = forms.FloatField(label='Variable 9.1', required=False)
    var139_2 = forms.FloatField(label='Variable 9.2', required=False)
    var139_3 = forms.FloatField(label='Variable 9.3', required=False)
    var139_4 = forms.FloatField(label='Variable 9.4', required=False)
    var139_5 = forms.FloatField(label='Variable 9.5', required=False)
    var139_6 = forms.FloatField(label='Variable 9.6', required=False)
    var139_7 = forms.FloatField(label='Variable 9.7', required=False)
    var139_8 = forms.FloatField(label='Variable 9.8', required=False)
    var139_9 = forms.FloatField(label='Variable 9.9', required=False)
    var139_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var140_1 = forms.FloatField(label='Variable 10.1', required=False)
    var140_2 = forms.FloatField(label='Variable 10.2', required=False)
    var140_3 = forms.FloatField(label='Variable 10.3', required=False)
    var140_4 = forms.FloatField(label='Variable 10.4', required=False)
    var140_5 = forms.FloatField(label='Variable 10.5', required=False)
    var140_6 = forms.FloatField(label='Variable 10.6', required=False)
    var140_7 = forms.FloatField(label='Variable 10.7', required=False)
    var140_8 = forms.FloatField(label='Variable 10.8', required=False)
    var140_9 = forms.FloatField(label='Variable 10.9', required=False)
    var140_10 = forms.FloatField(label='Variable 10.10', required=False)

    var141_1 = forms.FloatField(label='Variable 1.1', required=False)
    var141_2 = forms.FloatField(label='Variable 1.2', required=False)
    var141_3 = forms.FloatField(label='Variable 1.3', required=False)
    var141_4 = forms.FloatField(label='Variable 1.4', required=False)
    var141_5 = forms.FloatField(label='Variable 1.5', required=False)
    var141_6 = forms.FloatField(label='Variable 1.6', required=False)
    var141_7 = forms.FloatField(label='Variable 1.7', required=False)
    var141_8 = forms.FloatField(label='Variable 1.8', required=False)
    var141_9 = forms.FloatField(label='Variable 1.9', required=False)
    var141_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var142_1 = forms.FloatField(label='Variable 2.1', required=False)
    var142_2 = forms.FloatField(label='Variable 2.2', required=False)
    var142_3 = forms.FloatField(label='Variable 2.3', required=False)
    var142_4 = forms.FloatField(label='Variable 2.4', required=False)
    var142_5 = forms.FloatField(label='Variable 2.5', required=False)
    var142_6 = forms.FloatField(label='Variable 2.6', required=False)
    var142_7 = forms.FloatField(label='Variable 2.7', required=False)
    var142_8 = forms.FloatField(label='Variable 2.8', required=False)
    var142_9 = forms.FloatField(label='Variable 2.9', required=False)
    var142_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var143_1 = forms.FloatField(label='Variable 3.1', required=False)
    var143_2 = forms.FloatField(label='Variable 3.2', required=False)
    var143_3 = forms.FloatField(label='Variable 3.3', required=False)
    var143_4 = forms.FloatField(label='Variable 3.4', required=False)
    var143_5 = forms.FloatField(label='Variable 3.5', required=False)
    var143_6 = forms.FloatField(label='Variable 3.6', required=False)
    var143_7 = forms.FloatField(label='Variable 3.7', required=False)
    var143_8 = forms.FloatField(label='Variable 3.8', required=False)
    var143_9 = forms.FloatField(label='Variable 3.9', required=False)
    var143_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var144_1 = forms.FloatField(label='Variable 4.1', required=False)
    var144_2 = forms.FloatField(label='Variable 4.2', required=False)
    var144_3 = forms.FloatField(label='Variable 4.3', required=False)
    var144_4 = forms.FloatField(label='Variable 4.4', required=False)
    var144_5 = forms.FloatField(label='Variable 4.5', required=False)
    var144_6 = forms.FloatField(label='Variable 4.6', required=False)
    var144_7 = forms.FloatField(label='Variable 4.7', required=False)
    var144_8 = forms.FloatField(label='Variable 4.8', required=False)
    var144_9 = forms.FloatField(label='Variable 4.9', required=False)
    var144_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var145_1 = forms.FloatField(label='Variable 5.1', required=False)
    var145_2 = forms.FloatField(label='Variable 5.2', required=False)
    var145_3 = forms.FloatField(label='Variable 5.3', required=False)
    var145_4 = forms.FloatField(label='Variable 5.4', required=False)
    var145_5 = forms.FloatField(label='Variable 5.5', required=False)
    var145_6 = forms.FloatField(label='Variable 5.6', required=False)
    var145_7 = forms.FloatField(label='Variable 5.7', required=False)
    var145_8 = forms.FloatField(label='Variable 5.8', required=False)
    var145_9 = forms.FloatField(label='Variable 5.9', required=False)
    var145_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var146_1 = forms.FloatField(label='Variable 6.1', required=False)
    var146_2 = forms.FloatField(label='Variable 6.2', required=False)
    var146_3 = forms.FloatField(label='Variable 6.3', required=False)
    var146_4 = forms.FloatField(label='Variable 6.4', required=False)
    var146_5 = forms.FloatField(label='Variable 6.5', required=False)
    var146_6 = forms.FloatField(label='Variable 6.6', required=False)
    var146_7 = forms.FloatField(label='Variable 6.7', required=False)
    var146_8 = forms.FloatField(label='Variable 6.8', required=False)
    var146_9 = forms.FloatField(label='Variable 6.9', required=False)
    var146_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var147_1 = forms.FloatField(label='Variable 7.1', required=False)
    var147_2 = forms.FloatField(label='Variable 7.2', required=False)
    var147_3 = forms.FloatField(label='Variable 7.3', required=False)
    var147_4 = forms.FloatField(label='Variable 7.4', required=False)
    var147_5 = forms.FloatField(label='Variable 7.5', required=False)
    var147_6 = forms.FloatField(label='Variable 7.6', required=False)
    var147_7 = forms.FloatField(label='Variable 7.7', required=False)
    var147_8 = forms.FloatField(label='Variable 7.8', required=False)
    var147_9 = forms.FloatField(label='Variable 7.9', required=False)
    var147_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var148_1 = forms.FloatField(label='Variable 8.1', required=False)
    var148_2 = forms.FloatField(label='Variable 8.2', required=False)
    var148_3 = forms.FloatField(label='Variable 8.3', required=False)
    var148_4 = forms.FloatField(label='Variable 8.4', required=False)
    var148_5 = forms.FloatField(label='Variable 8.5', required=False)
    var148_6 = forms.FloatField(label='Variable 8.6', required=False)
    var148_7 = forms.FloatField(label='Variable 8.7', required=False)
    var148_8 = forms.FloatField(label='Variable 8.8', required=False)
    var148_9 = forms.FloatField(label='Variable 8.9', required=False)
    var148_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var149_1 = forms.FloatField(label='Variable 9.1', required=False)
    var149_2 = forms.FloatField(label='Variable 9.2', required=False)
    var149_3 = forms.FloatField(label='Variable 9.3', required=False)
    var149_4 = forms.FloatField(label='Variable 9.4', required=False)
    var149_5 = forms.FloatField(label='Variable 9.5', required=False)
    var149_6 = forms.FloatField(label='Variable 9.6', required=False)
    var149_7 = forms.FloatField(label='Variable 9.7', required=False)
    var149_8 = forms.FloatField(label='Variable 9.8', required=False)
    var149_9 = forms.FloatField(label='Variable 9.9', required=False)
    var149_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var150_1 = forms.FloatField(label='Variable 10.1', required=False)
    var150_2 = forms.FloatField(label='Variable 10.2', required=False)
    var150_3 = forms.FloatField(label='Variable 10.3', required=False)
    var150_4 = forms.FloatField(label='Variable 10.4', required=False)
    var150_5 = forms.FloatField(label='Variable 10.5', required=False)
    var150_6 = forms.FloatField(label='Variable 10.6', required=False)
    var150_7 = forms.FloatField(label='Variable 10.7', required=False)
    var150_8 = forms.FloatField(label='Variable 10.8', required=False)
    var150_9 = forms.FloatField(label='Variable 10.9', required=False)
    var150_10 = forms.FloatField(label='Variable 10.10', required=False)

    var151_1 = forms.FloatField(label='Variable 1.1', required=False)
    var151_2 = forms.FloatField(label='Variable 1.2', required=False)
    var151_3 = forms.FloatField(label='Variable 1.3', required=False)
    var151_4 = forms.FloatField(label='Variable 1.4', required=False)
    var151_5 = forms.FloatField(label='Variable 1.5', required=False)
    var151_6 = forms.FloatField(label='Variable 1.6', required=False)
    var151_7 = forms.FloatField(label='Variable 1.7', required=False)
    var151_8 = forms.FloatField(label='Variable 1.8', required=False)
    var151_9 = forms.FloatField(label='Variable 1.9', required=False)
    var151_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var152_1 = forms.FloatField(label='Variable 2.1', required=False)
    var152_2 = forms.FloatField(label='Variable 2.2', required=False)
    var152_3 = forms.FloatField(label='Variable 2.3', required=False)
    var152_4 = forms.FloatField(label='Variable 2.4', required=False)
    var152_5 = forms.FloatField(label='Variable 2.5', required=False)
    var152_6 = forms.FloatField(label='Variable 2.6', required=False)
    var152_7 = forms.FloatField(label='Variable 2.7', required=False)
    var152_8 = forms.FloatField(label='Variable 2.8', required=False)
    var152_9 = forms.FloatField(label='Variable 2.9', required=False)
    var152_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var153_1 = forms.FloatField(label='Variable 3.1', required=False)
    var153_2 = forms.FloatField(label='Variable 3.2', required=False)
    var153_3 = forms.FloatField(label='Variable 3.3', required=False)
    var153_4 = forms.FloatField(label='Variable 3.4', required=False)
    var153_5 = forms.FloatField(label='Variable 3.5', required=False)
    var153_6 = forms.FloatField(label='Variable 3.6', required=False)
    var153_7 = forms.FloatField(label='Variable 3.7', required=False)
    var153_8 = forms.FloatField(label='Variable 3.8', required=False)
    var153_9 = forms.FloatField(label='Variable 3.9', required=False)
    var153_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var154_1 = forms.FloatField(label='Variable 4.1', required=False)
    var154_2 = forms.FloatField(label='Variable 4.2', required=False)
    var154_3 = forms.FloatField(label='Variable 4.3', required=False)
    var154_4 = forms.FloatField(label='Variable 4.4', required=False)
    var154_5 = forms.FloatField(label='Variable 4.5', required=False)
    var154_6 = forms.FloatField(label='Variable 4.6', required=False)
    var154_7 = forms.FloatField(label='Variable 4.7', required=False)
    var154_8 = forms.FloatField(label='Variable 4.8', required=False)
    var154_9 = forms.FloatField(label='Variable 4.9', required=False)
    var154_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var155_1 = forms.FloatField(label='Variable 5.1', required=False)
    var155_2 = forms.FloatField(label='Variable 5.2', required=False)
    var155_3 = forms.FloatField(label='Variable 5.3', required=False)
    var155_4 = forms.FloatField(label='Variable 5.4', required=False)
    var155_5 = forms.FloatField(label='Variable 5.5', required=False)
    var155_6 = forms.FloatField(label='Variable 5.6', required=False)
    var155_7 = forms.FloatField(label='Variable 5.7', required=False)
    var155_8 = forms.FloatField(label='Variable 5.8', required=False)
    var155_9 = forms.FloatField(label='Variable 5.9', required=False)
    var155_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var156_1 = forms.FloatField(label='Variable 6.1', required=False)
    var156_2 = forms.FloatField(label='Variable 6.2', required=False)
    var156_3 = forms.FloatField(label='Variable 6.3', required=False)
    var156_4 = forms.FloatField(label='Variable 6.4', required=False)
    var156_5 = forms.FloatField(label='Variable 6.5', required=False)
    var156_6 = forms.FloatField(label='Variable 6.6', required=False)
    var156_7 = forms.FloatField(label='Variable 6.7', required=False)
    var156_8 = forms.FloatField(label='Variable 6.8', required=False)
    var156_9 = forms.FloatField(label='Variable 6.9', required=False)
    var156_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var157_1 = forms.FloatField(label='Variable 7.1', required=False)
    var157_2 = forms.FloatField(label='Variable 7.2', required=False)
    var157_3 = forms.FloatField(label='Variable 7.3', required=False)
    var157_4 = forms.FloatField(label='Variable 7.4', required=False)
    var157_5 = forms.FloatField(label='Variable 7.5', required=False)
    var157_6 = forms.FloatField(label='Variable 7.6', required=False)
    var157_7 = forms.FloatField(label='Variable 7.7', required=False)
    var157_8 = forms.FloatField(label='Variable 7.8', required=False)
    var157_9 = forms.FloatField(label='Variable 7.9', required=False)
    var157_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var158_1 = forms.FloatField(label='Variable 8.1', required=False)
    var158_2 = forms.FloatField(label='Variable 8.2', required=False)
    var158_3 = forms.FloatField(label='Variable 8.3', required=False)
    var158_4 = forms.FloatField(label='Variable 8.4', required=False)
    var158_5 = forms.FloatField(label='Variable 8.5', required=False)
    var158_6 = forms.FloatField(label='Variable 8.6', required=False)
    var158_7 = forms.FloatField(label='Variable 8.7', required=False)
    var158_8 = forms.FloatField(label='Variable 8.8', required=False)
    var158_9 = forms.FloatField(label='Variable 8.9', required=False)
    var158_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var159_1 = forms.FloatField(label='Variable 9.1', required=False)
    var159_2 = forms.FloatField(label='Variable 9.2', required=False)
    var159_3 = forms.FloatField(label='Variable 9.3', required=False)
    var159_4 = forms.FloatField(label='Variable 9.4', required=False)
    var159_5 = forms.FloatField(label='Variable 9.5', required=False)
    var159_6 = forms.FloatField(label='Variable 9.6', required=False)
    var159_7 = forms.FloatField(label='Variable 9.7', required=False)
    var159_8 = forms.FloatField(label='Variable 9.8', required=False)
    var159_9 = forms.FloatField(label='Variable 9.9', required=False)
    var159_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var160_1 = forms.FloatField(label='Variable 10.1', required=False)
    var160_2 = forms.FloatField(label='Variable 10.2', required=False)
    var160_3 = forms.FloatField(label='Variable 10.3', required=False)
    var160_4 = forms.FloatField(label='Variable 10.4', required=False)
    var160_5 = forms.FloatField(label='Variable 10.5', required=False)
    var160_6 = forms.FloatField(label='Variable 10.6', required=False)
    var160_7 = forms.FloatField(label='Variable 10.7', required=False)
    var160_8 = forms.FloatField(label='Variable 10.8', required=False)
    var160_9 = forms.FloatField(label='Variable 10.9', required=False)
    var160_10 = forms.FloatField(label='Variable 10.10', required=False)

    var161_1 = forms.FloatField(label='Variable 1.1', required=False)
    var161_2 = forms.FloatField(label='Variable 1.2', required=False)
    var161_3 = forms.FloatField(label='Variable 1.3', required=False)
    var161_4 = forms.FloatField(label='Variable 1.4', required=False)
    var161_5 = forms.FloatField(label='Variable 1.5', required=False)
    var161_6 = forms.FloatField(label='Variable 1.6', required=False)
    var161_7 = forms.FloatField(label='Variable 1.7', required=False)
    var161_8 = forms.FloatField(label='Variable 1.8', required=False)
    var161_9 = forms.FloatField(label='Variable 1.9', required=False)
    var161_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var162_1 = forms.FloatField(label='Variable 2.1', required=False)
    var162_2 = forms.FloatField(label='Variable 2.2', required=False)
    var162_3 = forms.FloatField(label='Variable 2.3', required=False)
    var162_4 = forms.FloatField(label='Variable 2.4', required=False)
    var162_5 = forms.FloatField(label='Variable 2.5', required=False)
    var162_6 = forms.FloatField(label='Variable 2.6', required=False)
    var162_7 = forms.FloatField(label='Variable 2.7', required=False)
    var162_8 = forms.FloatField(label='Variable 2.8', required=False)
    var162_9 = forms.FloatField(label='Variable 2.9', required=False)
    var162_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var163_1 = forms.FloatField(label='Variable 3.1', required=False)
    var163_2 = forms.FloatField(label='Variable 3.2', required=False)
    var163_3 = forms.FloatField(label='Variable 3.3', required=False)
    var163_4 = forms.FloatField(label='Variable 3.4', required=False)
    var163_5 = forms.FloatField(label='Variable 3.5', required=False)
    var163_6 = forms.FloatField(label='Variable 3.6', required=False)
    var163_7 = forms.FloatField(label='Variable 3.7', required=False)
    var163_8 = forms.FloatField(label='Variable 3.8', required=False)
    var163_9 = forms.FloatField(label='Variable 3.9', required=False)
    var163_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var164_1 = forms.FloatField(label='Variable 4.1', required=False)
    var164_2 = forms.FloatField(label='Variable 4.2', required=False)
    var164_3 = forms.FloatField(label='Variable 4.3', required=False)
    var164_4 = forms.FloatField(label='Variable 4.4', required=False)
    var164_5 = forms.FloatField(label='Variable 4.5', required=False)
    var164_6 = forms.FloatField(label='Variable 4.6', required=False)
    var164_7 = forms.FloatField(label='Variable 4.7', required=False)
    var164_8 = forms.FloatField(label='Variable 4.8', required=False)
    var164_9 = forms.FloatField(label='Variable 4.9', required=False)
    var164_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var165_1 = forms.FloatField(label='Variable 5.1', required=False)
    var165_2 = forms.FloatField(label='Variable 5.2', required=False)
    var165_3 = forms.FloatField(label='Variable 5.3', required=False)
    var165_4 = forms.FloatField(label='Variable 5.4', required=False)
    var165_5 = forms.FloatField(label='Variable 5.5', required=False)
    var165_6 = forms.FloatField(label='Variable 5.6', required=False)
    var165_7 = forms.FloatField(label='Variable 5.7', required=False)
    var165_8 = forms.FloatField(label='Variable 5.8', required=False)
    var165_9 = forms.FloatField(label='Variable 5.9', required=False)
    var165_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var166_1 = forms.FloatField(label='Variable 6.1', required=False)
    var166_2 = forms.FloatField(label='Variable 6.2', required=False)
    var166_3 = forms.FloatField(label='Variable 6.3', required=False)
    var166_4 = forms.FloatField(label='Variable 6.4', required=False)
    var166_5 = forms.FloatField(label='Variable 6.5', required=False)
    var166_6 = forms.FloatField(label='Variable 6.6', required=False)
    var166_7 = forms.FloatField(label='Variable 6.7', required=False)
    var166_8 = forms.FloatField(label='Variable 6.8', required=False)
    var166_9 = forms.FloatField(label='Variable 6.9', required=False)
    var166_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var167_1 = forms.FloatField(label='Variable 7.1', required=False)
    var167_2 = forms.FloatField(label='Variable 7.2', required=False)
    var167_3 = forms.FloatField(label='Variable 7.3', required=False)
    var167_4 = forms.FloatField(label='Variable 7.4', required=False)
    var167_5 = forms.FloatField(label='Variable 7.5', required=False)
    var167_6 = forms.FloatField(label='Variable 7.6', required=False)
    var167_7 = forms.FloatField(label='Variable 7.7', required=False)
    var167_8 = forms.FloatField(label='Variable 7.8', required=False)
    var167_9 = forms.FloatField(label='Variable 7.9', required=False)
    var167_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var168_1 = forms.FloatField(label='Variable 8.1', required=False)
    var168_2 = forms.FloatField(label='Variable 8.2', required=False)
    var168_3 = forms.FloatField(label='Variable 8.3', required=False)
    var168_4 = forms.FloatField(label='Variable 8.4', required=False)
    var168_5 = forms.FloatField(label='Variable 8.5', required=False)
    var168_6 = forms.FloatField(label='Variable 8.6', required=False)
    var168_7 = forms.FloatField(label='Variable 8.7', required=False)
    var168_8 = forms.FloatField(label='Variable 8.8', required=False)
    var168_9 = forms.FloatField(label='Variable 8.9', required=False)
    var168_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var169_1 = forms.FloatField(label='Variable 9.1', required=False)
    var169_2 = forms.FloatField(label='Variable 9.2', required=False)
    var169_3 = forms.FloatField(label='Variable 9.3', required=False)
    var169_4 = forms.FloatField(label='Variable 9.4', required=False)
    var169_5 = forms.FloatField(label='Variable 9.5', required=False)
    var169_6 = forms.FloatField(label='Variable 9.6', required=False)
    var169_7 = forms.FloatField(label='Variable 9.7', required=False)
    var169_8 = forms.FloatField(label='Variable 9.8', required=False)
    var169_9 = forms.FloatField(label='Variable 9.9', required=False)
    var169_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var170_1 = forms.FloatField(label='Variable 10.1', required=False)
    var170_2 = forms.FloatField(label='Variable 10.2', required=False)
    var170_3 = forms.FloatField(label='Variable 10.3', required=False)
    var170_4 = forms.FloatField(label='Variable 10.4', required=False)
    var170_5 = forms.FloatField(label='Variable 10.5', required=False)
    var170_6 = forms.FloatField(label='Variable 10.6', required=False)
    var170_7 = forms.FloatField(label='Variable 10.7', required=False)
    var170_8 = forms.FloatField(label='Variable 10.8', required=False)
    var170_9 = forms.FloatField(label='Variable 10.9', required=False)
    var170_10 = forms.FloatField(label='Variable 10.10', required=False)

    var171_1 = forms.FloatField(label='Variable 1.1', required=False)
    var171_2 = forms.FloatField(label='Variable 1.2', required=False)
    var171_3 = forms.FloatField(label='Variable 1.3', required=False)
    var171_4 = forms.FloatField(label='Variable 1.4', required=False)
    var171_5 = forms.FloatField(label='Variable 1.5', required=False)
    var171_6 = forms.FloatField(label='Variable 1.6', required=False)
    var171_7 = forms.FloatField(label='Variable 1.7', required=False)
    var171_8 = forms.FloatField(label='Variable 1.8', required=False)
    var171_9 = forms.FloatField(label='Variable 1.9', required=False)
    var171_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var172_1 = forms.FloatField(label='Variable 2.1', required=False)
    var172_2 = forms.FloatField(label='Variable 2.2', required=False)
    var172_3 = forms.FloatField(label='Variable 2.3', required=False)
    var172_4 = forms.FloatField(label='Variable 2.4', required=False)
    var172_5 = forms.FloatField(label='Variable 2.5', required=False)
    var172_6 = forms.FloatField(label='Variable 2.6', required=False)
    var172_7 = forms.FloatField(label='Variable 2.7', required=False)
    var172_8 = forms.FloatField(label='Variable 2.8', required=False)
    var172_9 = forms.FloatField(label='Variable 2.9', required=False)
    var172_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var173_1 = forms.FloatField(label='Variable 3.1', required=False)
    var173_2 = forms.FloatField(label='Variable 3.2', required=False)
    var173_3 = forms.FloatField(label='Variable 3.3', required=False)
    var173_4 = forms.FloatField(label='Variable 3.4', required=False)
    var173_5 = forms.FloatField(label='Variable 3.5', required=False)
    var173_6 = forms.FloatField(label='Variable 3.6', required=False)
    var173_7 = forms.FloatField(label='Variable 3.7', required=False)
    var173_8 = forms.FloatField(label='Variable 3.8', required=False)
    var173_9 = forms.FloatField(label='Variable 3.9', required=False)
    var173_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var174_1 = forms.FloatField(label='Variable 4.1', required=False)
    var174_2 = forms.FloatField(label='Variable 4.2', required=False)
    var174_3 = forms.FloatField(label='Variable 4.3', required=False)
    var174_4 = forms.FloatField(label='Variable 4.4', required=False)
    var174_5 = forms.FloatField(label='Variable 4.5', required=False)
    var174_6 = forms.FloatField(label='Variable 4.6', required=False)
    var174_7 = forms.FloatField(label='Variable 4.7', required=False)
    var174_8 = forms.FloatField(label='Variable 4.8', required=False)
    var174_9 = forms.FloatField(label='Variable 4.9', required=False)
    var174_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var175_1 = forms.FloatField(label='Variable 5.1', required=False)
    var175_2 = forms.FloatField(label='Variable 5.2', required=False)
    var175_3 = forms.FloatField(label='Variable 5.3', required=False)
    var175_4 = forms.FloatField(label='Variable 5.4', required=False)
    var175_5 = forms.FloatField(label='Variable 5.5', required=False)
    var175_6 = forms.FloatField(label='Variable 5.6', required=False)
    var175_7 = forms.FloatField(label='Variable 5.7', required=False)
    var175_8 = forms.FloatField(label='Variable 5.8', required=False)
    var175_9 = forms.FloatField(label='Variable 5.9', required=False)
    var175_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var176_1 = forms.FloatField(label='Variable 6.1', required=False)
    var176_2 = forms.FloatField(label='Variable 6.2', required=False)
    var176_3 = forms.FloatField(label='Variable 6.3', required=False)
    var176_4 = forms.FloatField(label='Variable 6.4', required=False)
    var176_5 = forms.FloatField(label='Variable 6.5', required=False)
    var176_6 = forms.FloatField(label='Variable 6.6', required=False)
    var176_7 = forms.FloatField(label='Variable 6.7', required=False)
    var176_8 = forms.FloatField(label='Variable 6.8', required=False)
    var176_9 = forms.FloatField(label='Variable 6.9', required=False)
    var176_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var177_1 = forms.FloatField(label='Variable 7.1', required=False)
    var177_2 = forms.FloatField(label='Variable 7.2', required=False)
    var177_3 = forms.FloatField(label='Variable 7.3', required=False)
    var177_4 = forms.FloatField(label='Variable 7.4', required=False)
    var177_5 = forms.FloatField(label='Variable 7.5', required=False)
    var177_6 = forms.FloatField(label='Variable 7.6', required=False)
    var177_7 = forms.FloatField(label='Variable 7.7', required=False)
    var177_8 = forms.FloatField(label='Variable 7.8', required=False)
    var177_9 = forms.FloatField(label='Variable 7.9', required=False)
    var177_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var178_1 = forms.FloatField(label='Variable 8.1', required=False)
    var178_2 = forms.FloatField(label='Variable 8.2', required=False)
    var178_3 = forms.FloatField(label='Variable 8.3', required=False)
    var178_4 = forms.FloatField(label='Variable 8.4', required=False)
    var178_5 = forms.FloatField(label='Variable 8.5', required=False)
    var178_6 = forms.FloatField(label='Variable 8.6', required=False)
    var178_7 = forms.FloatField(label='Variable 8.7', required=False)
    var178_8 = forms.FloatField(label='Variable 8.8', required=False)
    var178_9 = forms.FloatField(label='Variable 8.9', required=False)
    var178_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var179_1 = forms.FloatField(label='Variable 9.1', required=False)
    var179_2 = forms.FloatField(label='Variable 9.2', required=False)
    var179_3 = forms.FloatField(label='Variable 9.3', required=False)
    var179_4 = forms.FloatField(label='Variable 9.4', required=False)
    var179_5 = forms.FloatField(label='Variable 9.5', required=False)
    var79_6 = forms.FloatField(label='Variable 9.6', required=False)
    var179_7 = forms.FloatField(label='Variable 9.7', required=False)
    var179_8 = forms.FloatField(label='Variable 9.8', required=False)
    var179_9 = forms.FloatField(label='Variable 9.9', required=False)
    var179_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var180_1 = forms.FloatField(label='Variable 10.1', required=False)
    var180_2 = forms.FloatField(label='Variable 10.2', required=False)
    var180_3 = forms.FloatField(label='Variable 10.3', required=False)
    var180_4 = forms.FloatField(label='Variable 10.4', required=False)
    var180_5 = forms.FloatField(label='Variable 10.5', required=False)
    var180_6 = forms.FloatField(label='Variable 10.6', required=False)
    var180_7 = forms.FloatField(label='Variable 10.7', required=False)
    var180_8 = forms.FloatField(label='Variable 10.8', required=False)
    var180_9 = forms.FloatField(label='Variable 10.9', required=False)
    var180_10 = forms.FloatField(label='Variable 10.10', required=False)

    var181_1 = forms.FloatField(label='Variable 1.1', required=False)
    var181_2 = forms.FloatField(label='Variable 1.2', required=False)
    var181_3 = forms.FloatField(label='Variable 1.3', required=False)
    var181_4 = forms.FloatField(label='Variable 1.4', required=False)
    var181_5 = forms.FloatField(label='Variable 1.5', required=False)
    var181_6 = forms.FloatField(label='Variable 1.6', required=False)
    var181_7 = forms.FloatField(label='Variable 1.7', required=False)
    var181_8 = forms.FloatField(label='Variable 1.8', required=False)
    var181_9 = forms.FloatField(label='Variable 1.9', required=False)
    var181_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var182_1 = forms.FloatField(label='Variable 2.1', required=False)
    var182_2 = forms.FloatField(label='Variable 2.2', required=False)
    var182_3 = forms.FloatField(label='Variable 2.3', required=False)
    var182_4 = forms.FloatField(label='Variable 2.4', required=False)
    var182_5 = forms.FloatField(label='Variable 2.5', required=False)
    var182_6 = forms.FloatField(label='Variable 2.6', required=False)
    var182_7 = forms.FloatField(label='Variable 2.7', required=False)
    var182_8 = forms.FloatField(label='Variable 2.8', required=False)
    var182_9 = forms.FloatField(label='Variable 2.9', required=False)
    var182_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var183_1 = forms.FloatField(label='Variable 3.1', required=False)
    var183_2 = forms.FloatField(label='Variable 3.2', required=False)
    var183_3 = forms.FloatField(label='Variable 3.3', required=False)
    var183_4 = forms.FloatField(label='Variable 3.4', required=False)
    var183_5 = forms.FloatField(label='Variable 3.5', required=False)
    var183_6 = forms.FloatField(label='Variable 3.6', required=False)
    var183_7 = forms.FloatField(label='Variable 3.7', required=False)
    var183_8 = forms.FloatField(label='Variable 3.8', required=False)
    var183_9 = forms.FloatField(label='Variable 3.9', required=False)
    var183_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var184_1 = forms.FloatField(label='Variable 4.1', required=False)
    var184_2 = forms.FloatField(label='Variable 4.2', required=False)
    var184_3 = forms.FloatField(label='Variable 4.3', required=False)
    var184_4 = forms.FloatField(label='Variable 4.4', required=False)
    var184_5 = forms.FloatField(label='Variable 4.5', required=False)
    var184_6 = forms.FloatField(label='Variable 4.6', required=False)
    var184_7 = forms.FloatField(label='Variable 4.7', required=False)
    var184_8 = forms.FloatField(label='Variable 4.8', required=False)
    var184_9 = forms.FloatField(label='Variable 4.9', required=False)
    var184_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var185_1 = forms.FloatField(label='Variable 5.1', required=False)
    var185_2 = forms.FloatField(label='Variable 5.2', required=False)
    var185_3 = forms.FloatField(label='Variable 5.3', required=False)
    var185_4 = forms.FloatField(label='Variable 5.4', required=False)
    var185_5 = forms.FloatField(label='Variable 5.5', required=False)
    var185_6 = forms.FloatField(label='Variable 5.6', required=False)
    var185_7 = forms.FloatField(label='Variable 5.7', required=False)
    var185_8 = forms.FloatField(label='Variable 5.8', required=False)
    var185_9 = forms.FloatField(label='Variable 5.9', required=False)
    var185_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var186_1 = forms.FloatField(label='Variable 6.1', required=False)
    var186_2 = forms.FloatField(label='Variable 6.2', required=False)
    var186_3 = forms.FloatField(label='Variable 6.3', required=False)
    var186_4 = forms.FloatField(label='Variable 6.4', required=False)
    var186_5 = forms.FloatField(label='Variable 6.5', required=False)
    var186_6 = forms.FloatField(label='Variable 6.6', required=False)
    var186_7 = forms.FloatField(label='Variable 6.7', required=False)
    var186_8 = forms.FloatField(label='Variable 6.8', required=False)
    var186_9 = forms.FloatField(label='Variable 6.9', required=False)
    var186_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var187_1 = forms.FloatField(label='Variable 7.1', required=False)
    var187_2 = forms.FloatField(label='Variable 7.2', required=False)
    var187_3 = forms.FloatField(label='Variable 7.3', required=False)
    var187_4 = forms.FloatField(label='Variable 7.4', required=False)
    var187_5 = forms.FloatField(label='Variable 7.5', required=False)
    var187_6 = forms.FloatField(label='Variable 7.6', required=False)
    var187_7 = forms.FloatField(label='Variable 7.7', required=False)
    var187_8 = forms.FloatField(label='Variable 7.8', required=False)
    var187_9 = forms.FloatField(label='Variable 7.9', required=False)
    var187_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var188_1 = forms.FloatField(label='Variable 8.1', required=False)
    var188_2 = forms.FloatField(label='Variable 8.2', required=False)
    var188_3 = forms.FloatField(label='Variable 8.3', required=False)
    var188_4 = forms.FloatField(label='Variable 8.4', required=False)
    var188_5 = forms.FloatField(label='Variable 8.5', required=False)
    var188_6 = forms.FloatField(label='Variable 8.6', required=False)
    var188_7 = forms.FloatField(label='Variable 8.7', required=False)
    var188_8 = forms.FloatField(label='Variable 8.8', required=False)
    var188_9 = forms.FloatField(label='Variable 8.9', required=False)
    var188_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var189_1 = forms.FloatField(label='Variable 9.1', required=False)
    var189_2 = forms.FloatField(label='Variable 9.2', required=False)
    var189_3 = forms.FloatField(label='Variable 9.3', required=False)
    var189_4 = forms.FloatField(label='Variable 9.4', required=False)
    var189_5 = forms.FloatField(label='Variable 9.5', required=False)
    var189_6 = forms.FloatField(label='Variable 9.6', required=False)
    var189_7 = forms.FloatField(label='Variable 9.7', required=False)
    var189_8 = forms.FloatField(label='Variable 9.8', required=False)
    var189_9 = forms.FloatField(label='Variable 9.9', required=False)
    var189_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var190_1 = forms.FloatField(label='Variable 10.1', required=False)
    var190_2 = forms.FloatField(label='Variable 10.2', required=False)
    var190_3 = forms.FloatField(label='Variable 10.3', required=False)
    var190_4 = forms.FloatField(label='Variable 10.4', required=False)
    var190_5 = forms.FloatField(label='Variable 10.5', required=False)
    var190_6 = forms.FloatField(label='Variable 10.6', required=False)
    var190_7 = forms.FloatField(label='Variable 10.7', required=False)
    var190_8 = forms.FloatField(label='Variable 10.8', required=False)
    var190_9 = forms.FloatField(label='Variable 10.9', required=False)
    var190_10 = forms.FloatField(label='Variable 10.10', required=False)


    var191_1 = forms.FloatField(label='Variable 1.1', required=False)
    var191_2 = forms.FloatField(label='Variable 1.2', required=False)
    var191_3 = forms.FloatField(label='Variable 1.3', required=False)
    var191_4 = forms.FloatField(label='Variable 1.4', required=False)
    var191_5 = forms.FloatField(label='Variable 1.5', required=False)
    var191_6 = forms.FloatField(label='Variable 1.6', required=False)
    var191_7 = forms.FloatField(label='Variable 1.7', required=False)
    var191_8 = forms.FloatField(label='Variable 1.8', required=False)
    var191_9 = forms.FloatField(label='Variable 1.9', required=False)
    var191_10 = forms.FloatField(label='Variable 1.10', required=False)

    #variable 2
    var192_1 = forms.FloatField(label='Variable 2.1', required=False)
    var192_2 = forms.FloatField(label='Variable 2.2', required=False)
    var192_3 = forms.FloatField(label='Variable 2.3', required=False)
    var192_4 = forms.FloatField(label='Variable 2.4', required=False)
    var192_5 = forms.FloatField(label='Variable 2.5', required=False)
    var192_6 = forms.FloatField(label='Variable 2.6', required=False)
    var192_7 = forms.FloatField(label='Variable 2.7', required=False)
    var192_8 = forms.FloatField(label='Variable 2.8', required=False)
    var192_9 = forms.FloatField(label='Variable 2.9', required=False)
    var192_10 = forms.FloatField(label='Variable 2.10', required=False)

    #variable 3
    var193_1 = forms.FloatField(label='Variable 3.1', required=False)
    var193_2 = forms.FloatField(label='Variable 3.2', required=False)
    var193_3 = forms.FloatField(label='Variable 3.3', required=False)
    var193_4 = forms.FloatField(label='Variable 3.4', required=False)
    var193_5 = forms.FloatField(label='Variable 3.5', required=False)
    var193_6 = forms.FloatField(label='Variable 3.6', required=False)
    var193_7 = forms.FloatField(label='Variable 3.7', required=False)
    var193_8 = forms.FloatField(label='Variable 3.8', required=False)
    var193_9 = forms.FloatField(label='Variable 3.9', required=False)
    var193_10 = forms.FloatField(label='Variable 3.10', required=False)

    #variable 4
    var194_1 = forms.FloatField(label='Variable 4.1', required=False)
    var194_2 = forms.FloatField(label='Variable 4.2', required=False)
    var194_3 = forms.FloatField(label='Variable 4.3', required=False)
    var194_4 = forms.FloatField(label='Variable 4.4', required=False)
    var194_5 = forms.FloatField(label='Variable 4.5', required=False)
    var194_6 = forms.FloatField(label='Variable 4.6', required=False)
    var194_7 = forms.FloatField(label='Variable 4.7', required=False)
    var194_8 = forms.FloatField(label='Variable 4.8', required=False)
    var194_9 = forms.FloatField(label='Variable 4.9', required=False)
    var194_10 = forms.FloatField(label='Variable 4.10', required=False)

    #variable 5
    var195_1 = forms.FloatField(label='Variable 5.1', required=False)
    var195_2 = forms.FloatField(label='Variable 5.2', required=False)
    var195_3 = forms.FloatField(label='Variable 5.3', required=False)
    var195_4 = forms.FloatField(label='Variable 5.4', required=False)
    var195_5 = forms.FloatField(label='Variable 5.5', required=False)
    var195_6 = forms.FloatField(label='Variable 5.6', required=False)
    var195_7 = forms.FloatField(label='Variable 5.7', required=False)
    var195_8 = forms.FloatField(label='Variable 5.8', required=False)
    var195_9 = forms.FloatField(label='Variable 5.9', required=False)
    var195_10 = forms.FloatField(label='Variable 5.10', required=False)

    #variable 6
    var196_1 = forms.FloatField(label='Variable 6.1', required=False)
    var196_2 = forms.FloatField(label='Variable 6.2', required=False)
    var196_3 = forms.FloatField(label='Variable 6.3', required=False)
    var196_4 = forms.FloatField(label='Variable 6.4', required=False)
    var196_5 = forms.FloatField(label='Variable 6.5', required=False)
    var196_6 = forms.FloatField(label='Variable 6.6', required=False)
    var196_7 = forms.FloatField(label='Variable 6.7', required=False)
    var196_8 = forms.FloatField(label='Variable 6.8', required=False)
    var196_9 = forms.FloatField(label='Variable 6.9', required=False)
    var196_10 = forms.FloatField(label='Variable 6.10', required=False)

    #variable 7
    var197_1 = forms.FloatField(label='Variable 7.1', required=False)
    var197_2 = forms.FloatField(label='Variable 7.2', required=False)
    var197_3 = forms.FloatField(label='Variable 7.3', required=False)
    var197_4 = forms.FloatField(label='Variable 7.4', required=False)
    var197_5 = forms.FloatField(label='Variable 7.5', required=False)
    var197_6 = forms.FloatField(label='Variable 7.6', required=False)
    var197_7 = forms.FloatField(label='Variable 7.7', required=False)
    var197_8 = forms.FloatField(label='Variable 7.8', required=False)
    var197_9 = forms.FloatField(label='Variable 7.9', required=False)
    var197_10 = forms.FloatField(label='Variable 7.10', required=False)

    #variable 8
    var198_1 = forms.FloatField(label='Variable 8.1', required=False)
    var198_2 = forms.FloatField(label='Variable 8.2', required=False)
    var198_3 = forms.FloatField(label='Variable 8.3', required=False)
    var198_4 = forms.FloatField(label='Variable 8.4', required=False)
    var198_5 = forms.FloatField(label='Variable 8.5', required=False)
    var198_6 = forms.FloatField(label='Variable 8.6', required=False)
    var198_7 = forms.FloatField(label='Variable 8.7', required=False)
    var198_8 = forms.FloatField(label='Variable 8.8', required=False)
    var198_9 = forms.FloatField(label='Variable 8.9', required=False)
    var198_10 = forms.FloatField(label='Variable 8.10', required=False)

    #variable 9
    var199_1 = forms.FloatField(label='Variable 9.1', required=False)
    var199_2 = forms.FloatField(label='Variable 9.2', required=False)
    var199_3 = forms.FloatField(label='Variable 9.3', required=False)
    var199_4 = forms.FloatField(label='Variable 9.4', required=False)
    var199_5 = forms.FloatField(label='Variable 9.5', required=False)
    var199_6 = forms.FloatField(label='Variable 9.6', required=False)
    var199_7 = forms.FloatField(label='Variable 9.7', required=False)
    var199_8 = forms.FloatField(label='Variable 9.8', required=False)
    var199_9 = forms.FloatField(label='Variable 9.9', required=False)
    var199_10 = forms.FloatField(label='Variable 9.10', required=False)

    #variable 10
    var200_1 = forms.FloatField(label='Variable 10.1', required=False)
    var200_2 = forms.FloatField(label='Variable 10.2', required=False)
    var200_3 = forms.FloatField(label='Variable 10.3', required=False)
    var200_4 = forms.FloatField(label='Variable 10.4', required=False)
    var200_5 = forms.FloatField(label='Variable 10.5', required=False)
    var200_6 = forms.FloatField(label='Variable 10.6', required=False)
    var200_7 = forms.FloatField(label='Variable 10.7', required=False)
    var200_8 = forms.FloatField(label='Variable 10.8', required=False)
    var200_9 = forms.FloatField(label='Variable 10.9', required=False)
    var200_10 = forms.FloatField(label='Variable 10.10', required=False)
