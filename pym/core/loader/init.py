import sys
from .finder import PreprocessPyFinder
from pathlib import Path

def init(root: Path) -> None:
    "Function to set the Pym module preproccessor for PYSX files."
    if not any(isinstance(f, PreprocessPyFinder) for f in sys.meta_path):
        sys.meta_path.insert(0, PreprocessPyFinder(root))