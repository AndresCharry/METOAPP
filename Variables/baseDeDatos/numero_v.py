import pandas as pd

def datos():
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    df = int(df['Numero de variables'][0])
    return df

def nom_var():
    nombre_variables = {}
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/Variables.csv', header=0)
    try:
        nombre_variables['variable1'] = df.at[0,'variable1']
        nombre_variables['variable2'] = df.at[0,'variable2']
        nombre_variables['variable3'] = df.at[0,'variable3']
        nombre_variables['variable4'] = df.at[0,'variable4']
        nombre_variables['variable5'] = df.at[0,'variable5']
        nombre_variables['variable6'] = df.at[0,'variable6']
        nombre_variables['variable7'] = df.at[0,'variable7']
        nombre_variables['variable8'] = df.at[0,'variable8']
        nombre_variables['variable9'] = df.at[0,'variable9']
        nombre_variables['variable10'] = df.at[0,'variable10']
        nombre_variables['variable11'] = df.at[0,'variable11']
        nombre_variables['variable12'] = df.at[0,'variable12']
        nombre_variables['variable13'] = df.at[0,'variable13']
        nombre_variables['variable14'] = df.at[0,'variable14']
        nombre_variables['variable15'] = df.at[0,'variable15']
        nombre_variables['variable16'] = df.at[0,'variable16']
        nombre_variables['variable17'] = df.at[0,'variable17']
        nombre_variables['variable18'] = df.at[0,'variable18']
        nombre_variables['variable19'] = df.at[0,'variable19']
        nombre_variables['variable20'] = df.at[0,'variable20']
    except:
        pass

    return nombre_variables

def num_var():
    variables = {}
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/Variables.csv', header=0, index_col= False)
    try:
        variables['num_variable1'] = int(df['num_variable1'])
        variables['num_variable2'] = int(df['num_variable2'])
        variables['num_variable3'] = int(df['num_variable3'])
        variables['num_variable4'] = int(df['num_variable4'])
        variables['num_variable5'] = int(df['num_variable5'])
        variables['num_variable6'] = int(df['num_variable6'])
        variables['num_variable7'] = int(df['num_variable7'])
        variables['num_variable8'] = int(df['num_variable8'])
        variables['num_variable9'] = int(df['num_variable9'])
        variables['num_variable10'] = int(df['num_variable10'])
        variables['num_variable11'] = int(df['num_variable11'])
        variables['num_variable12'] = int(df['num_variable12'])
        variables['num_variable13'] = int(df['num_variable13'])
        variables['num_variable14'] = int(df['num_variable14'])
        variables['num_variable15'] = int(df['num_variable15'])
        variables['num_variable16'] = int(df['num_variable16'])
        variables['num_variable17'] = int(df['num_variable17'])
        variables['num_variable18'] = int(df['num_variable18'])
        variables['num_variable19'] = int(df['num_variable19'])
        variables['num_variable20'] = int(df['num_variable20'])
    except:
        pass

    return variables
