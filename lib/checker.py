from modules.database_search import search
from lib.validator import url_to_domain

class LinkInfo():
    
    def __init__(self, url: str) -> None:
        
        self.url: str = url
        
    def database_search(self) -> bool | dict:

        domain = url_to_domain(self.url)
        results = search(domain)

        if results is not False:
            return results

        else:

            return False
        
    def path_search(self) -> bool:
        
        try:
            
            pass
            
        except Exception as e:
            
            return False 
        
        
    def thread_scan(self) -> bool:
        
        try:
            
            pass
            
        except Exception as e:
            
            return False       
        