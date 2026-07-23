# Server config
from .config import SERVER

VERSION = '1.0'
"Server module version"

# Import simple make
from .make import make

__all__ = ['SERVER', 'make']