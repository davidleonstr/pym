# Module that renders the pym code
from pym.core.render import Render

# Module that generates the constants for GET, POST, etc. parameters
from .integrations.params import params

# Function to send responses
from .integrations.send import send

# Enconding used to read/write files
from pym.core.config import encoding, suffix

# Integrated server config, ppym files suffix, mime-types used for http responses,
# suffix used for static resources
from .config import SERVER, MIMETYPES, SUFFIXRESOURCES

# Funtion to write logs in file
from pym.server.utils import log

# Pym modules loader (preprocess .py files before getting)
from pym.core.loader.finder import PreprocessPyFinder

from pathlib import Path
import sys

# Class for handling responses in context
from .basics import Response

# Used to manage exit
from pym.core import language
from pym.core import init

LOA = {
    'base': False
}
"""
Dictionary to register loaded steps.
"""

# WSGI enterpoint
def application(environ, start_response):
    index = None

    # Object for handling responses in context
    presponse = Response()

    log('Creating parameters based in request.')

    # Creating params
    PARAMS = params(environ)

    # Context for pym
    context = {}
    context.update(PARAMS)
    context['response'] = presponse

    # Base path
    if not LOA['base']:
        log('Setting base path for server.')
        LOA['base'] = Path(SERVER['start-folder']).resolve()

    # Request path
    path = environ.get('PATH_INFO', '/')
    resource = LOA['base'] if path == '/' else LOA['base'] / path.lstrip('/')

    # favicon
    if path == '/favicon.ico':
        presponse.modstatus('204 No Content')
        presponse.body = b''
        return send(presponse, start_response)

    # STATIC RESOURCES
    if resource.suffix in SUFFIXRESOURCES:
        log(f"Serving resource: '{resource}'.")

        try:
            try:
                data = open(resource, encoding=encoding).read().encode(encoding)
            except UnicodeDecodeError:
                data = open(resource, 'rb').read()
        except FileNotFoundError:
            presponse.modstatus('404 File not found')
            presponse.body = b''
            return send(presponse, start_response)

        presponse.modstatus('200 OK')
        presponse.header('Content-Type', SUFFIXRESOURCES[resource.suffix])
        presponse.body = data
        return send(presponse, start_response)

    # FOLDER SEARCHING
    if SERVER['use-folder-searching']:
        log('Using server folder searching.')

        if resource.is_file():
            index = resource
        elif resource.is_dir():
            for file in resource.iterdir():
                if file.is_file() and file.name.lower().startswith('index'):
                    index = file
                    break

        if index is None:
            presponse.modstatus('404 File not found')
            presponse.body = b''
            return send(presponse, start_response)

    else:
        index = Path(LOA['base'] / SERVER['start-point']).resolve()

    # READ INDEX
    try:
        text = open(index, encoding=encoding).read()
    except FileNotFoundError:
        presponse.modstatus('404 File not found')
        presponse.body = b''
        return send(presponse, start_response)

    # ROOT FOR INCLUDES
    root = Path(LOA['base']).resolve()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    # RENDER
    if index.suffix == suffix:
        if not any(isinstance(f, PreprocessPyFinder) for f in sys.meta_path):
            log('Setting up Python module preprocessor.')
            init(LOA['base'])

        render = Render(context=context, filename=index)
        try:
            html = render.get(text).encode(encoding)
        except language.Exit:
            return send(presponse, start_response)
    else:
        html = text.encode(encoding)

    presponse.modstatus('200 OK')
    presponse.header('Content-Type', MIMETYPES[index.suffix])
    presponse.body = html

    return send(presponse, start_response)