import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.validator import gen_id
    from app import _get_database

db = _get_database()['links']['list']


class Link:

    def __init__(self, url: str, malicious: bool, nsfw: bool, malware: bool, phishing: bool, ip_logging: bool) -> None:

        self.id = gen_id()
        self.url: str = url
        self.malicious: bool = malicious
        self.nsfw: bool = nsfw
        self.malware: bool = malware
        self.phishing: bool = phishing
        self.ip_logging: bool = ip_logging
        self.added_at: datetime.datetime = datetime.datetime.utcnow()

    def add(self) -> None:

        try:

            db.insert_one({

                '_id': self.id,
                'url': self.url,
                'malicious': self.malicious,
                'nsfw': self.nsfw,
                'malware': self.malware,
                'phishing': self.phishing,
                'ip_logging': self.ip_logging,
                'added_at': self.added_at

            })

            return None

        except Exception as e:
            print(e)
