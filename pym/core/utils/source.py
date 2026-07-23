import sys
import os

def source(path: str, file: str) -> str:
    """
    Obtain any resource from the project, regardless of whether it is packaged.
    """
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(file))

    return os.path.abspath(os.path.join(base, path))