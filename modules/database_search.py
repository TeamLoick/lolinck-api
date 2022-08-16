from app import _get_database
from models.log_model import Log

db = _get_database()['links']['list']


def search(domain: str) -> dict | bool:
    """
        Returns the search results from the given domain

                Parameters:
                        domain (str): Domain to search

                Returns:
                        dict: Database results or None if no results were found
    """

    s = db.find_one({'url': domain})

    try:

        Log(False, s['url'], s['malicious'], s['nsfw'], s['malware'], s['phishing'], s['ip_logging']).add()
        return {'url': s['url'], 'malicious': s['malicious'], 'nsfw': s['nsfw'], 'malware': s['malware'],
                'phishing': s['phishing'], 'ip_logging': s['ip_logging']}

    except TypeError:
        return False
