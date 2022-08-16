import socket
import uuid


# noinspection PyBroadException
def site_active(url: str) -> bool:
    """
        Check if the site is registered

                Parameters:
                        url (str): URL to check for registration

                Returns:
                        bool: True or False depending on whether the site is registered or not
    """

    # noinspection PyBroadException
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
    """
        Check if the domain has valid syntax

                Parameters:
                        url (str): URL to check for registration

                Returns:
                        bool: True or False depending on whether the site is valid or not
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


def url_to_domain(url: str) -> str:
    """
        Get the domain from the url

                Parameters:
                        url (str): The url to get the domain from

                Returns:
                        d (str): The domain name
    """

    d: str = url.lower()

    if url.startswith('http://') or url.startswith('https://'):
        d = d.split('/')[2]

    if d.endswith('/'):
        d = d.split('/')[0]

    return d


def gen_id() -> str:
    """
        Generate unique id

                Returns:
                        str: The unique id generated
    """

    return str(uuid.uuid4())
