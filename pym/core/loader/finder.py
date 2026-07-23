import importlib.util
from pathlib import Path
from .config import CACHE
from .loader import PreprocessedPyLoader
from pym.core.imports import imports
from pym.core.config import pysxSuffix

class PreprocessPyFinder(importlib.abc.MetaPathFinder):
    def __init__(self, root: Path):
        self.root = root

    def find_spec(self, fullname, path=None, target=None):
        relBase = fullname.replace('.', '/')

        extensions = ['.py', pysxSuffix]
        file = None

        for ext in extensions:
            candidate = self.root / f'{relBase}{ext}'
            if candidate.exists():
                file = candidate
                break

        if file is None:
            return None

        key = file.resolve()

        if key not in CACHE:
            raw = file.read_text(encoding='utf-8')
            CACHE[key] = imports(raw, file)

        loader = PreprocessedPyLoader(CACHE[key], file)
        return importlib.util.spec_from_loader(fullname, loader)