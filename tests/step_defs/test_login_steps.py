import pytest
from pytest_bdd import given, when, then, parsers

from src.actions.navigate import Navigate
from src.actor.stage import Stage
from src.actor.actor import Actor
from src.abilities.browse_the_web import BrowseTheWeb
from src.questions.confirmacion_mensaje import ConfirmacionMensaje
from src.tasks.login import LoginPractice
from src.tasks.logout import Logout
from support.config_variables import Config

@pytest.fixture
def app_state():
    return {"opened": False, "user": None, "result": None}

@given('que el usuario "TestUser" está en la página de login')
def user_on_login(page):
    actor = Actor.named("TestUser_SQA").can(BrowseTheWeb.using(page))
    Stage.set_the_stage(actor)
    actor.attempts_to( Navigate.to(Config.get_base_url()))

@when('ingresa las credenciales válidas')
def user_enters_valid_credentials():
    actor = Stage.the_actor_in_the_spotlight()
    actor.attempts_to(LoginPractice.with_credentials(Config.get_username(), Config.get_password()))

@then(parsers.parse('debería ver el mensaje de bienvenida "{expected_message}"'))
def user_sees_welcome_message(expected_message):
    actor = Stage.the_actor_in_the_spotlight()
    mensaje = actor.ask(ConfirmacionMensaje.displayed())
    assert expected_message.lower() in mensaje.lower(), \
        f"No se encontró la confirmación. Mensaje obtenido: {mensaje}"

@then('debería ver el botón de logout')
def user_sees_logout_button():
    actor = Stage.the_actor_in_the_spotlight()
    actor.attempts_to(Logout().session())