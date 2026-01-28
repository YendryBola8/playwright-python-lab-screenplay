from src.abilities.browse_the_web import BrowseTheWeb
from src.actor.actor import Performable, Actor

class Fill(Performable):

    def __init__(self, selector: str):
        self.selector = selector
        self.value = ""

    @classmethod
    def field(cls, selector: str) -> "Fill":
        return cls(selector)

    def with_value(self, value: str) -> "Fill":
        self.value = value
        return self

    def perform_as(self, actor: Actor) -> None:
        page = actor.using(BrowseTheWeb).page
        page.fill(self.selector, self.value)