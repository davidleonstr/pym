import importlib.abc

class PreprocessedPyLoader(importlib.abc.Loader):
    def __init__(self, source, file):
        self.source = source
        self.file = file

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        module.__file__ = str(self.file)
        exec(self.source, module.__dict__)