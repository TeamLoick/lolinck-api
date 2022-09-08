from app import _get_database
from cachetools import cached, TTLCache

db = _get_database()['links']['list']


@cached(cache=TTLCache(maxsize=10, ttl=86400))
def search(domain: str) -> dict | None:
    """
        Returns the search results from the given domain

                Parameters:
                        domain (str): Domain to search

                Returns:
                        dict: Database results or None if no results were found
    """

    s = db.find_one({'url': domain})

    try:

        return {'url': s['url'], 'malicious': s['malicious'], 'nsfw': s['nsfw'], 'malware': s['malware'],
                'phishing': s['phishing'], 'ip_logging': s['ip_logging']}

    except TypeError:
        return None
