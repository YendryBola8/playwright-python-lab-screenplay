from src.actor.actor import Performable, Actor
from src.abilities.browse_the_web import BrowseTheWeb
from typing import Optional

class Click(Performable):

    def __init__(self, selector: str, index: Optional[int] = None):
        self.selector = selector
        self.index = index

    @classmethod
    def on(cls, selector: str, index: Optional[int] = None) -> "Click":
        return cls(selector, index)

    def perform_as(self, actor: Actor) -> None:
        page = actor.using(BrowseTheWeb).page
        if self.index is not None:
            elements = page.locator(self.selector)
            elements.nth(self.index).click()
        else:
            # Click simple
            page.click(self.selector)