Feature: Autenticación de usuarios
  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a mi cuenta

  @login @smoke @regression @critical @positive @ui @e2e
  Scenario: Login exitoso con credenciales válidas
    Given que el usuario "TestUser" está en la página de login
    When ingresa las credenciales válidas
    Then debería ver el mensaje de bienvenida "Logged In Successfully"
    And debería ver el botón de logout


#  Scenario Outline: Login con múltiples credenciales
#    Given que el usuario "<nombre>" está en la página de login
#    When ingresa el usuario "<username>" y contraseña "<password>"
#    Then debería ver "<resultado>"
#
#    Examples:
#      | nombre    | username  | password     | resultado                |
#      | Usuario1  | student   | Password123  | Logged In Successfully   |
#      | Usuario2  | wronguser | Password123  | Your username is invalid!|
#      | Usuario3  | student   | wrongpass    | Your password is invalid!|