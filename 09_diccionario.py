mi_diccionario = {
  'llave1': 1,
  'llave2': 'Hola a todos!!',
  'llave3': True
}

print( mi_diccionario )
print(mi_diccionario['llave2'] )

usuario = {
  'nombre': 'Uziel',
  'apellidos': 'Trujillo Colon',
  'telefono': {
    'casa': '12321631',
    'celular': '99999234234'
  },
  'lenguajes': [ 'php', 'JAVA', 'C', 'Python' ],
}

for key, value in usuario['telefono'].items():
  print( "[%s]: %s" %(key, value) )

print( usuario['telefono']['casa'] )
print( usuario['lenguajes'][3] )
# print("==================")
# print( usuario )
# # Imprimiendo llaves
# for llave in usuario.keys():
#   print( "LLave %s" %(llave) )

# print("==================")
# # Imprimiendo Valores
# for valor in usuario.values():
#   print( "Valor %s" %(valor) )

# print("==================")
# # Imprimiendo llave y valor
# for llave, valor in usuario.items():
#   print( "llave %s: Valor %s" %(llave, valor) )