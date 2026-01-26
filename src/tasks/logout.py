from src.actions.click import Click
from src.actor.actor import Performable, Actor
from src.ui.practice import Practice

class Logout(Performable):

    def __init__(self):
        pass

    @classmethod
    def session(cls) -> "Logout":
        return cls()

    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Click.on(Practice.LOGOUT_LINK)
        )