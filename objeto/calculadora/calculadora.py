class Calculadora:
  def __init__(self, numero1, numero2):
    self.numero1 = numero1
    self.numero2 = numero2
    print('Se ejecuto el constructor')
  
  def suma( self, numero1, numero2 ):
    print( numero1 + numero2 )
  
  def resta( self, numero1, numero2 ):
    return numero1 - numero2
  
  def multiplicacion(self):
    print( self.numero1 * self.numero2 )