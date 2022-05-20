valores = ( "Python", True, 5, 3.1416, True, True )

print( type(valores) )
print( valores[1] )
print( valores.count(True) )
print( valores.index(True) )
print( len( valores ) )

for item in valores:
  print( "Valor %s" %( item ) )