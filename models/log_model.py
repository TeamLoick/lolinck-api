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
    
    def __init__(self, new: bool, url: str, malicious: bool, nsfw: bool, malware: bool, phishing: bool, ip_logging: bool) -> None:
        
        self.new: bool = new
        self.url: str = url
        self.malicious: bool = malicious
        self.nsfw: bool = nsfw
        self.malware: bool = malware
        self.phishing: bool = phishing
        self.ip_logging: bool = ip_logging
    
    def add(self) -> None:
        
        try:
        
            db.insert_one({
                "DATE": datetime.datetime.now(),
                "URL": self.url,
                "NEW": self.new,
                "MALICIOUS": self.malicious,
                "NSFW": self.nsfw,
                "MALWARE": self.malware,
                "PHISHING": self.phishing,
                "IP_LOGGING": self.ip_logging
            })
            
        except:
        
            return None
        
