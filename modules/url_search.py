from json import load
from metadata_parser import MetadataParser, NotParsableFetchError
from lib.validator import get_status_code
from datetime import datetime
from difflib import SequenceMatcher
from os.path import split
from tldextract import extract


class URlSearch:

    @staticmethod
    def nsfw(url: str) -> bool:
        """
            **

                    Parameters:
                            url (str): Domain to search

                    Returns:
                            dict: Path results for the given domain
        """

        with open("../commons/nsfw_keywords.json", "r") as file:
            nsfw_keys = load(file)

        xxx_suffixes = ['xxx', 'adult', 'porn', 'sex']
        extracted_url = extract(url)

        for x in xxx_suffixes:
            if x in extracted_url.suffix:
                return True

        for x in nsfw_keys:
            if x in extracted_url.domain:
                return True

        for x in nsfw_keys:
            if x in extracted_url.subdomain:
                return True

        for x in nsfw_keys:
            if x in split(url):
                return True

        if get_status_code(url) != 200:
            return False

        try:

            #www = MetadataParser(url=url,
            #                     search_head_only=False,
            #                     support_malformed=True,
            #                     force_doctype=True)

            #_title_ = www.metadata['page']['title']
            #_description_ = www.get_metadatas('description')
            #_keywords_ = www.get_metadatas('keywords')
            
            _title_ = soup.find("meta",  property="og:title", content=True)
            _description_ = soup.find("meta",  property="og:title", content=True)
            _keywords_ = soup.find("meta",  property="og:title", content=True)

            if _keywords_ is not None:
                for x in _keywords_:
                    x[0].split()
                    for y in nsfw_keys:
                        if y in x:
                            return True

            if _description_ is not None:
                for x in _description_:
                    x[0].split()
                    for y in nsfw_keys:
                        if y in x:
                            return True

            if _m_title_ is not None:
                for x in _m_title_:
                    x[0].split()
                    for y in nsfw_keys:
                        if y in x:
                            return True

            if _title_ is not None:
                for x in _title_:
                    x[0].split()
                    for y in nsfw_keys:
                        if y in x:
                            return True

            return False

        except NotParsableFetchError:
            return False

        except IndexError:
            return False

    @staticmethod
    def phishing(url: str) -> bool:
        """
            **

                    Parameters:
                            url (str): Domain to search

                    Returns:
                            dict: Path results for the given domain
        """

        domain = extract(url)
        return domain.subdomain, domain.domain, domain.suffix

        # PATH

        # OTHERS


u = URlSearch()
print(u.nsfw('https://fr.pornhub.com'))
