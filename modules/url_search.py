import aiohttp
import asyncio
from json import load
from tldextract import extract
import warnings
from os.path import split
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from bs4.dammit import EncodingDetector
from typing import TYPE_CHECKING, Dict
from urllib.parse import urlparse

warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)

if TYPE_CHECKING:
    from lib.validator import get_status_code


async def Scrapper(url: str,
                   NSFW=False,
                   PHISHING=False,
                   MALWARE=False,
                   IPLOGGER=False) -> dict[str, bool]:
    async with aiohttp.ClientSession() as session:

        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
            'Content-Type': 'text/html'
        }

        async with session.get(url=url, headers=headers, ssl=False) as resp:

            body = await resp.text()
            # print(await resp.text())
            soup = BeautifulSoup(body, 'html.parser')

            # Be very carefull with the keywords, our api only use specific keywords
            # Using every term like ['porn', 'sex'] will cause false positives.
            # Our keywords avoid 99% false positives. (25k Keywords in total)
            # Our keywords are totally private.

            with open("./commons/nsfw/keywords.json", "r") as file:
                nsfw_keywords = load(file)

            with open("./commons/nsfw/meta_keywords.json", "r") as file:
                nsfw_meta_keywords = load(file)

            with open("./commons/nsfw/suffixes.json", "r") as file:
                nsfw_suffixes = load(file)

            with open("./commons/nsfw/paths.json", "r") as file:
                nsfw_paths = load(file)

            ####

            extracted_url = extract(url)

            for x in nsfw_suffixes:
                if x in extracted_url.suffix:
                    NSFW = True

            for x in nsfw_suffixes:
                if x in extracted_url.domain:
                    NSFW = True

            for x in nsfw_suffixes:
                if x in extracted_url.subdomain:
                    NSFW = True

            for x in nsfw_paths:
                if x in urlparse(url).path:
                    NSFW = True

            try:

                _title_ = soup.find("meta",
                                    {"property": "og:title"})["content"]

                if _title_ is not None:
                    if any(x in _title_ for x in nsfw_keywords):
                        NSFW = True

            except IndexError:
                pass

            except TypeError:
                pass

            try:
                _description_ = soup.find("meta",
                                          {"property": "og:description"})["content"]

                if _description_ is not None:
                    if any(x in _description_ for x in nsfw_keywords):
                        NSFW = True

            except IndexError:
                pass

            except TypeError:
                pass

            try:

                _keywords_ = soup.find("meta",
                                       {'name': 'keywords'})["content"]

                if _keywords_ is not None:
                    if any(x in _keywords_ for x in nsfw_meta_keywords):
                        NSFW = True


            except IndexError:
                pass

            except TypeError:
                pass

            for x in soup.find_all("img", alt=True):
                for y in nsfw_keywords:
                    if y in x['alt']:
                        NSFW = True

            for x in soup.find_all("a"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            for x in soup.find_all("span"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            for x in soup.find_all("h1"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            for x in soup.find_all("h2"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            for x in soup.find_all("h3"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            for x in soup.find_all("div"):
                for y in nsfw_keywords:
                    if y in x.text:
                        NSFW = True

            # Detect NSFW SubReddits (100% Acurracy)
            if soup.find_all("div",
                             {"class": "_2GSkrIFkojWV3L0GzQPQ78"}):
                NSFW = True

            # Find RTA Image
            if soup.find('img', alt='RTA'):
                NSFW = True

            elif soup.find('img', alt='RTA image'):
                NSFW = True

            elif soup.find('img', alt='RTAimage'):
                NSFW = True

            elif soup.find('img', alt='RTA img'):
                NSFW = True

            elif soup.find('img', alt='RTA icon'):
                NSFW = True

            elif soup.find('img', alt='RTA badge'):
                NSFW = True

            elif soup.find('img', {'class': 'rta'}):
                NSFW = True

            # Return by default False
            return {
                'NSFW': NSFW,
                'PHISHING': PHISHING,
                'IPLOGGER': IPLOGGER,
                'MALWARE': MALWARE
            }
