9import random

numeroAleatorio = random.randint( 0, 30 )
# edad = int( input("Escribe tu edad: ") )

# if( edad > 18 ):
#   print("Eres mayor de edad")
# elif( edad == 18 ):
#   print("Eres mayor de edad recientemente")
# else:
#   print("Hueles a MP 😁")

result = "Mayor de edad" if numeroAleatorio > 18 else "Menor de edad"
print( result, numeroAleatorio )