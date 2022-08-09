from app import _get_database
from models.log_model import Log

db = _get_database()['links']['list']


def search(domain: str) -> dict:
    
    s = db.find_one({'link': domain})
    
    try:
        
        if s['type'] == 'malware' or s['type'] == 'phishing':
            malicious = True 
        else:
            malicious = False
            
            
        if s['type'] == 'nsfw':
            nsfw = True
        else:
            nsfw = False
            
            
        Log(False, s['type'], s['link']).register()
            
        return {'malicious': malicious, 'nsfw': nsfw, 'link': s['link'], 'type': s['type']}
    
    except:
        
        return False
    