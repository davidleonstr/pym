import json

# Enconding used to read/write files
from pym.core.config import encoding

from pathlib import Path

CONFIGPATH = Path('./server.json').resolve()
"""
Path to the server's JSON configuration file.
"""

try:
    SERVER = json.loads(open(CONFIGPATH, encoding=encoding).read())
    """
    Server config JSON data.
    """
except:
    SERVER = {
        'local': {
            'host': 'localhost',
            'port': 8000
        },
        'start-folder': './',
        'use-folder-searching': True,
        'start-point': 'index.pym',
        'logs': False,
        'logs-file': 'log.log',
        'suffix-pages': [
            '.html',
            '.htm',
            '.pym'
        ],
        'MIMETYPES': {
            '.html': 'text/html',
            '.pym': 'text/html',
            '.htm': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.mjs': 'application/javascript',
            '.json': 'application/json',
            '.xml': 'application/xml',
            '.txt': 'text/plain',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.webp': 'image/webp',
            '.ico': 'image/x-icon',
            '.woff': 'font/woff',
            '.woff2': 'font/woff2',
            '.ttf': 'font/ttf',
            '.otf': 'font/otf',
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
            '.mp4': 'video/mp4',
            '.webm': 'video/webm',
            '.pdf': 'application/pdf',
            '.zip': 'application/zip'
        },
        'docs': {
            'start-point': 'Index (start point) file in start-folder.',
            'use-folder-searching': 'Define whether to use folder search via URL or redirect everything to the start point.',
            'middleware-exec': 'Path to the executable file responsible for handling the middleware.',
            'suffix-pages': 'Define which file suffixes are renderable pages.',
            'logs': 'Define whether the log file will be used.',
            'logs-file': 'Log file path.'
        },
        'from': 'assignement'
    }
    """
    Server config JSON data.
    """

MIMETYPES = SERVER['MIMETYPES']
"""
Server MIMEYPES.
"""
MIMETYPES: dict

SUFFIXRESOURCES = {
    k: v for k, v in MIMETYPES.items()
    if k not in SERVER['suffix-pages']
}
"""
Resource suffixes.
"""