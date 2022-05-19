nombre = 'Uziel Trujillo Colon'
print("Cadena original: %s" %(nombre) )

nombre = nombre.lower()
print("Nombre en minuscula: %s" %(nombre) )

nombre = nombre.upper()
print("Nombre en mayuscula: %s" %(nombre) )

nombre = nombre.capitalize()
print("Primera letra en mayuscula: %s" %(nombre) )

nombre = nombre.replace("t", "T")
print("Reemplazando letras: %s" %(nombre) )

print( "Posicion 1: %s" %( nombre[1] ) )

print( "Rango de cadena [0:5] %s" %( nombre[0:5] ) )

print( "Invertir cadena [::-1] %s" %( nombre[::-1] ) )

print( "Longitud de la cadena %i" %( len( nombre ) ) )