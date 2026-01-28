from src.actor.actor import Question, Actor
from src.abilities.browse_the_web import BrowseTheWeb
from src.ui.practice import Practice

class ConfirmacionMensaje(Question):

    def __init__(self):
        pass

    @classmethod
    def displayed(cls) -> "ConfirmacionMensaje":
        return cls()

    def answered_by(self, actor: Actor) -> str:
        text = actor.using(BrowseTheWeb).page.locator(Practice.SUCCESS_MESSAGE).inner_text().strip()
        return text or ""