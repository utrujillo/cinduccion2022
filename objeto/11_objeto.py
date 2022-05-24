from calculadora.calculadora import Calculadora

numero1 = 10
numero2 = 20
calc = Calculadora(numero1, numero2)


calc.suma( numero1, numero2 )
result = calc.resta( numero1, numero2 )
print( 'Resta %i' %(result) )

calc.multiplicacion()