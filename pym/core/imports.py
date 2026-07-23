from pathlib import Path

# Module that renders the pym code
from .render import Render
from pym.core.config import pysxSuffix

# Function responsible for preprocessing native Python code from .py and .pysx files
def imports(code: str, file: Path) -> str:
    # Envolve Pysx tags in code
    if file.suffix == pysxSuffix:
        return Render.envolve(code)
    
    return code