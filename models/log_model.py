import datetime
from app import _get_database

"""

Logging Privacy Policy

This privacy policy discloses the privacy practices for lolinck.xyz API

These logs are used to be able to have an activity of the new links and types of links identified, 
to be able to improve our systems and see if they are being effective.

Your ip or token is not displayed as an identifier for the scanned links
We only log the scanned links with the purpose of improving our detection system.
And they are not displayed with third parties or publicly, these logs are only viewed by our internal team.

Visit our privacy terms to learn everything we do with your information.
lolinck.xyz/privacy

"""

db = _get_database()['logs']['activity']

class Log():
    
    def __init__(self, new: bool, type: str, link: str) -> None:
        
        self.new = new
        self.type = type
        self.link = link
    
    def register(self) -> None:
        
        db.insert_one({
            "date": datetime.datetime.now(),
            "new": self.new,
            "type": self.type,
            "link": self.link
        })
        
        