# pip install pandas
import pandas as pd

data = {
  'edad': [10, 9, 10, 15, 13],
  'cm': [120, 150, 80, 170, 100],
  'pais': ['co', 'ec', 'mx', 'us', 'ar'],
  'genero': [ 'M', 'M', 'H', 'M', 'H' ],
  'Q1': [ 10, 9, 8, 10 , 8 ],
  'Q2': [ 9 , 9, 6, 6, 7 ]
}

# print( type( data ) )
# dataframe = pd.DataFrame( data )
# print( dataframe )

# Asignando indices
dataframe = pd.DataFrame( data, index=['Ana', 'Maria', 'Juan', 'Kyberly', 'Bryan'] )
print( dataframe )

# Obtener indices
print( dataframe.index )
# Obtener columnas
print( dataframe.columns )
# Obtener los valores
print( dataframe.values )

# Seleccionar datos de forma prticular
print( dataframe[ ['edad', 'genero'] ] )

# Seleccionar informacion por indice
print( dataframe.loc['Maria'] )

# Seleccionar informacion por indice y llave
print('==============')
print( dataframe.loc[ 'Maria' ]['Q1'] )

# Seleccionar todos las filas de campos especificos
print( dataframe.loc[:, ['edad', 'Q2']] )

# Filtrando informacion
print('==== Filtros =====')
print( dataframe['edad'] >= 10 )
print( dataframe[ dataframe['edad'] >= 10 ] )
print( dataframe.query( 'edad >= 10' ) )
print( dataframe.query( 'edad >= 10 & pais == "mx"' ) )