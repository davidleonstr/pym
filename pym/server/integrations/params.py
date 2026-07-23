from urllib.parse import parse_qs
from http.cookies import SimpleCookie

def params(environ) -> dict:
    # Get request method from environment variables of WSGI
    method = environ['REQUEST_METHOD']
    body = ''

    # It retrieves and processes the fields from GET request
    GET = parse_qs(environ.get('QUERY_STRING', ''))
    "Super global with the GET request data"

    # It retrieves and processes the fields from POST request
    POST = {}
    "Super global with the POST request data"
    if method == 'POST':
        length = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(length).decode()
        POST = parse_qs(body)

    cookie = SimpleCookie()
    # It retrieves and processes COOKIES from request
    cookie.load(environ.get('HTTP_COOKIE', ''))

    COOKIES = {k: v.value for k, v in cookie.items()}
    "Super global with the request COOKIES"

    REQUEST = {}
    "Super global with the GET, POST and COOKIES data"

    REQUEST.update(GET)
    REQUEST.update(POST)
    REQUEST.update(COOKIES)

    PATH = environ.get('PATH_INFO', '/')

    request = {
        'method': environ['REQUEST_METHOD'],
        'path': PATH,
        'query': {k: v[0] for k, v in parse_qs(environ.get('QUERY_STRING', '')).items()},
        'headers': {
            k[5:]: v for k, v in environ.items() if k.startswith('HTTP_')
        },
        'body': body,
        'pass': True
    }

    PARAMS = {
        'REQUEST': REQUEST,
        'GET': GET,
        'POST': POST,
        'COOKIES': COOKIES,
        'PATH': PATH,
        'raw-request': request # Used in middleware executables
    }
    """
    Super global constants available in server-rendered Pym code
    """

    return PARAMS

__all__ = ['params']