import argparse
from typing import Callable, Dict

# For command module:
# +----------------------------------------+
# |    Function -> Register -> Set Args    |
# +----------------------------------------+

parser = argparse.ArgumentParser(description='Pym parser.')
"Global parser."

subparsers = parser.add_subparsers(dest='utility', help='Available utilities.')
"Used to create parsers."

parsers = {}
parsers: Dict[str, argparse.ArgumentParser]
"Command parser."

utilities = {}
"Commands/utilities."

def register(name: str, callable: Callable, parser: argparse.ArgumentParser):
    """
    Function to register command and parser.
    """
    parsers[name] = parser
    utilities[name] = callable