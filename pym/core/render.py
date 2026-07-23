import io
import sys

# r-p = regex pattern
# Pym configuration, r-p for pym tags, r-p from includes tags, common r-p,
# r-p for single evaluation labels (ternaries), r-p for Pysx plugin
from .config import CONFIG, PATTERN, INCLUDE, COMMONS, EVALP, PYSX

# Module containing common pym utilities within code without importing
from pym.core import language

import textwrap

# Enconding used to read/write files
from .config import encoding

from pathlib import Path

# To have better exceptions
import traceback

class Render:
    def __init__(self, context: dict = None, filename: str | None = None) -> None:
        self.context = context or {}

        # Resolve root
        self.filename = Path(filename).resolve() if filename else None
        self.base = self.filename.parent if self.filename else Path.cwd()

        # Use language context (functions, objects, etc)
        self.context.update(language.context)
    
    # Read and insert include files code in template
    def includes(self, template: str) -> str:
        # For every pattern match
        def insert(match):
            try:
                # Open the include file and returns the code
                return open(self.base / Path(match.group(1).strip()), encoding=encoding).read()
            except Exception as e:
                # Returns pre-def exception
                e = traceback.format_exc()
                return CONFIG['language']['python-error-return'].format(e)
        
        # For every patter
        while INCLUDE.search(template):
            template = INCLUDE.sub(insert, template)
        
        # Template with includes
        return template
    
    # Method to envolve HTML tags
    @staticmethod
    def envolve(code: str) -> str:
        # For every pattern match
        def format(match):
            code = match.group(0)

            # Remove the () of the text
            code = code[1:-1]

            # Returns the code as a multiline string
            return CONFIG['language']['pysx-envolve'].format(code)

        # Envolve all HTML tags
        code = PYSX.sub(
            format, 
            code
        )

        return code

    # Eval one line
    def evaluate(self, template: str) -> str:
        def evalp(match):         
            expr = textwrap.dedent(match.group(1)).strip()

            # Envolve HTML tags
            expr = Render.envolve(expr)

            try:
                # Eval and returns the result
                return str(eval(expr, self.context))
            except Exception as e:
                # Returns pre-def exception
                e = traceback.format_exc()
                return CONFIG['language']['python-error-return'].format(e)
            
        return EVALP.sub(evalp, template)

    # Get the renderer template
    def get(self, template: str) -> str:
        def execute(match, buffer: io.StringIO):       
            code = textwrap.dedent(match.group(1)).strip()

            pos = buffer.tell()

            # Envolve HTML tags
            code = Render.envolve(code)

            try:
                # Execute code without restrictions
                exec(code, self.context)
            except language.Exit:
                raise language.Exit(buffer.getvalue())
            except Exception as e:
                # Write in buffer pre-def exception
                e = traceback.format_exc()
                print(CONFIG['language']['python-error-return'].format(e))

            delta = buffer.getvalue()[pos:]

            return delta
        
        # Process and insert code inclusions
        template = self.includes(template=template)
        
        # Save stdout copy
        stdout = sys.stdout

        # Get all printed text and save that in buffer
        sys.stdout = buffer = io.StringIO()

        try:
            # For every pym tag
            while PATTERN.search(template):
                template = PATTERN.sub(lambda match: execute(buffer=buffer, match=match), template)
        except language.Exit:
            raise
        finally:
            # Restore normal stdout
            sys.stdout = stdout

        # Evaluate single lines of code
        template = self.evaluate(template=template)

        # Delete extra lines in the HTML
        template = COMMONS['white-lines'].sub('\n', template)

        # Returns the final HTML
        return template

__all__ = ['Render']