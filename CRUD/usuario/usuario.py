import pandas as pd

class Usuario:
  def __init__(self):
    self.FILE = 'C:/Users/utrujillo/Desktop/induccion/CRUD/data.xlsx'
    self.usuarios = []
  
  def listar_usuarios(self):
    return self.usuarios
  
  def crear_usuario(self):
    print('++++++ Datos de usuario+++++')
    id = int( input('ID: ') )
    nombre = input('Nombre: ')
    apellidos = input('Apellidos: ')
    tipo = '''
      Administrador
      Inventario
      Ventas
    Seleccionar tipo de usuario:
    '''
    tipo_usuario = input(tipo)
    vis = '''
      True
      False
    Visibilidad del usuario:
    '''
    visible = input(vis)

    usuario = {
      id: id,
      nombre: nombre,
      apellidos: apellidos,
      tipo_usuario: tipo,
      visible: visible
    }

    self.usuarios.append( usuario )
    dataframe = pd.DataFrame( self.usuarios )
    dataframe.to_excel( self.FILE )
    print( dataframe )

    

