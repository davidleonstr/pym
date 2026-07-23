from .functions import echo, close
from .tag import TAG
from .exit import Exit

context = {
    'echo': echo,
    'TAG': TAG,
    'close': close,
    '__name__': '__main__',
    'INITAG': ''
}

__all__ = ['context', 'Exit']