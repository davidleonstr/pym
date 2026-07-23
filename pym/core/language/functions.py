import sys
from .exit import Exit

def echo(*args) -> None:
    """
    Function to print text.
    """
    sys.stdout.write(''.join(str(a) for a in args))

def close():
    """
    Stop template execution and immediately return the response.

    This does not terminate the process; it only aborts the current
    request rendering flow.
    """
    raise Exit