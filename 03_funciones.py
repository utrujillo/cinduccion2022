def saludo():
  print("Hola mundo")

  print( "Suma: %f" %( numero1 + numero2 ) )

def resta( numero1, numero2 ):
  return numero1 - numero2

numero1 = 10
numero2 = 25

saludo()
result = resta( numero1, numero2 )
print( "Resta: %f" %( result ) )
