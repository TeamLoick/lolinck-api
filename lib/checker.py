from modules.database_search import search
from lib.validator import url_to_domain


class LinkInfo:

    def __init__(self, url: str) -> None:

        self.url: str = url

    def database_search(self) -> bool | dict:

        domain = url_to_domain(self.url)
        results = search(domain)

        if results is not False:
            return results

        else:

            return False

    @staticmethod
    def path_search() -> bool:

        try:

            pass

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def thread_scan() -> bool:

        try:

            pass

        except Exception as e:
            print(e)
            return False
