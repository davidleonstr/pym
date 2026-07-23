from .__register__ import register, subparsers, parsers, utilities, parser

# Load command modules
from .serve import serve
from .version import version
from .config import config
# Add to trashss
__trash__ = [serve, version, config]

__all__ = ['register', 'subparsers', 'parsers', 'utilities', 'parser']