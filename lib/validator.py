import socket


def site_active(url: str) -> bool:
    
    """_summary_

    Args:
        url (_type_): string
        
    """
    
    try:
        
        domain = url.lower()
        
        if url.startswith('http://') or url.startswith('https://'):
            domain = url.split('/')[2]
            
        if domain.endswith('/'):
            domain = domain.split('/')[0]
        
        try:
            
            socket.gethostbyname(domain)
            
        except socket.gaierror:
            
            return False
        
        else:
            
            return True
        
    except Exception as e:
        
        return False
    

def domain_valid(url: str) -> bool:
    """_summary_

    Args:
        url (_type_): string
        
    """

    try:

        illeg_chars = [
            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ";", ":", ',',
            "?", "/", "=", "+", "<", ">", '\\'
        ]
        
        domain = url.lower()
        
        if url.startswith('http://') or url.startswith('https://'):
            domain = url.split('/')[2]
            
        if domain.endswith('/'):
            domain = domain.split('/')[0]

        if len(domain) > 255:
            return False

        if '.' not in domain:
            return False

        if ' ' in domain:
            return False

        if domain.split('.')[-1].isalpha() is False:
            return False

        for char in illeg_chars:
            if char in domain:
                return False
            
        return True

    except Exception as e:

        print(e)
        return False