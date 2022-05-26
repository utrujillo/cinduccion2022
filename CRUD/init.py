from usuario.usuario import Usuario

def menu():
  menu = '''
    **********************
      Curso induccion 😋
    **********************
    1. Listar usuarios
    2. Crear usuario
    3. Buscar por nombre de usuario
    4. Buscar por ID usuario
    5. Actualizar usuario
    6. Eliminar usuario

    Seleccionar una opcion: 
  '''
  # print(menu)
  opcion = int( input(menu) )
  return opcion

if __name__ == '__main__':

  usuario = Usuario()

  opcion = menu()

  if( opcion == 1 ):
    usurio.listar_usuarios()
  elif( opcion == 2 ):
    usuario.crear_usuario()
