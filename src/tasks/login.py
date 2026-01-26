from src.actions.click import Click
from src.actions.fill import Fill
from src.actor.actor import Performable, Actor
from src.ui.practice import Practice

class LoginPractice(Performable):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def with_credentials(cls, username: str, password: str) -> "LoginPractice":
        return cls(username, password)

    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Fill.field(Practice.USERNAME_INPUT).with_value(self.username),
            Fill.field(Practice.PASSWORD_INPUT).with_value(self.password),
            Click.on(Practice.SUBMIT_BUTTON)
        )