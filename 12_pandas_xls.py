import pandas as pd

data = {
  'edad': [10, 9, 10, 15, 13],
  'cm': [120, 150, 80, 170, 100],
  'pais': ['co', 'ec', 'mx', 'us', 'ar'],
  'genero': [ 'M', 'M', 'H', 'M', 'H' ],
  'Q1': [ 10, 9, 8, 10 , 8 ],
  'Q2': [ 9 , 9, 6, 6, 7 ]
}

dataframe = pd.DataFrame( data )

PATH = 'C:/Users/utrujillo/Desktop/induccion/{}'
# print( PATH.format('data.xlsx') )
# Guardar archivo en excel
# dataframe.to_excel( PATH.format('data.xlsx') )

# Leer el archivo de excel
data_from_xls = pd.read_excel( PATH.format('data.xlsx'), index_col=0 )
print( data_from_xls )