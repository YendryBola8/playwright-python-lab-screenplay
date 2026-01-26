from playwright.sync_api import Page

class BrowseTheWeb:
    
    def __init__(self, page: Page):
        self._page = page

    @classmethod
    def using(cls, page: Page) -> "BrowseTheWeb":
        return cls(page)

    @property
    def page(self) -> Page:
        return self._page