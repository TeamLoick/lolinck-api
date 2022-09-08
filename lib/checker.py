from modules.database_search import search
from lib.validator import url_to_domain


# noinspection PyPropertyDefinition
class LinkInfo:

    def __init__(self, url: str) -> None:
        self.url: str = url

    @property
    def results(self) -> str:
        pass
