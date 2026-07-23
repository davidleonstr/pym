# Register callable: Register command and parser
from pym.commands import subparsers, parsers, register

import json

# server.json
from pym.server.config import CONFIGPATH, SERVER

NAME = 'config'
"Command name."

# Command to execute one pym file
def config(args):
    # Set from
    SERVER['from'] = 'read'

    with open(args.output, 'w') as file:
        file.write(json.dumps(SERVER, indent=4))

# Register command and parser
register(
    name=NAME,
    callable=config,
    parser=subparsers.add_parser(NAME, help='Generate Pym server configuration.')
)

# Read this help
parsers[NAME].add_argument(
    '--output',
    '-o',
    required=False,
    type=str,
    default=CONFIGPATH,
    help=f"[Pym] Server configuration output. Default ('{CONFIGPATH}')"
)