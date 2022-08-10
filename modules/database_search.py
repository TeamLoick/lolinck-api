from app import _get_database
from models.log_model import Log

db = _get_database()['links']['list']


def search(domain: str) -> dict:
    
    s = db.find_one({'url': domain})
    
    try:
        
        Log(False, s['url'], s['malicious'], s['nsfw'], s['malware'], s['phishing'], s['ip_logging']).add()
            
        return {'URL': s['link'], 'MALICIOUS': s['malicious'], 'NSFW': s['nsfw'], 'MALWARE': s['malware'], 'PHISHING': s['phishing'], 'IP_LOGGING': s['ip_logging']}
    
    except:
        
        return False
    
    
