valores = [ "Python", True, 5, 3.1416, True, True ]

print( type(valores) )
print( valores[2] )

valores.append( 'Uziel' )
print( valores )
valores.pop(1)
print( valores )

for item in valores:
  print( "Valor %s" %(item) )

nuevosValores = [ 'Juan', True, 'Maria' ]
listaFinal = valores + nuevosValores
print( listaFinal )