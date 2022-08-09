import datetime
from app import _get_database

db = _get_database()['links']['list']

class Link():
    
    def __init__(self, type: str, link: str) -> None:
        
        self.type = type
        self.link = link
    
    def add(self) -> None:
        
        try:
            db.insert_one({
                "date": datetime.datetime.now(),
                "type": self.type,
                "link": self.link
            })
            
        except Exception as e:
            print(e)
        
        