from src.actor.actor import Performable, Actor
from src.abilities.browse_the_web import BrowseTheWeb

class Navigate(Performable):
    def __init__(self, url: str):
        self.url = url

    @classmethod
    def to(cls, url: str) -> "Navigate":
        return cls(url)

    def perform_as(self, actor: Actor) -> None:
        actor.using(BrowseTheWeb).page.goto(self.url)
        #print(f"🌐 Navegando a {self.url}")
