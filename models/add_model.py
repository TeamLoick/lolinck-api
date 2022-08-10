from app import _get_database

db = _get_database()['links']['list']

class Link():
    
    def __init__(self, url: str, malicious: bool, nsfw: bool, malware: bool, phishing: bool, ip_logging: bool) -> None:
        
        self.url: str = url
        self.malicious: bool = malicious
        self.nsfw: bool = nsfw
        self.malware: bool = malware
        self.phishing: bool = phishing
        self.ip_logging: bool = ip_logging
    
    def add(self) -> None:
        
        try:
            
            db.insert_one({
                "URL": self.url,    
                "MALICIOUS": self.malicious,
                "NSFW": self.nsfw,
                "MALWARE": self.malware,
                "PHISHING": self.phishing,
                "IP_LOGGING": self.ip_logging
            })
            
        except:
        
            return None
        
        
