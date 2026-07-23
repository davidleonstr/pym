# Integrated config module
import pym.server.config as config

# Integrated server module
import pym.server as server

# Funtion to write logs in file
from pym.server.utils import log

import argparse

# To have better error tracebacks
import traceback

# Console style
from colorama import Fore, Style

# Register callable: Register command and parser
from pym.commands import subparsers, parsers, register

NAME = 'serve'
"Command name."

# Making <serve> configuration
def serve(args):
    try:
        # Setting server star-folder
        config.SERVER['start-folder'] = args.tree

        # Server <host>, <port>
        host, port = args.host, args.port

        # Setting server host and server port
        config.SERVER['local']['host'] = host
        config.SERVER['local']['port'] = port

        # Setting server folder searching in config (FLAG)
        config.SERVER['use-folder-searching'] = args.folder_searching

        # Setting server index in config
        config.SERVER['start-point'] = args.index

        # Setting logs in config (FLAG)
        config.SERVER['logs'] = args.logs

        # Setting logs file path in config
        config.SERVER['logs-file'] = args.logs_path

        # Warning if it use default server config
        if config.SERVER['from'] != 'read':
            # Log for previous line
            log(
                f"Configuration file not found, the predefined dictionary is being used.",
                type='warning'
            )

        # Simple function to make the integrated server definite in server module __init__
        server.make({
            'host': host,
            'port': int(port)
        })
    except Exception:
        # Out application
        # Log if it failed
        log(
            traceback.format_exc(),
            type='error'
        )
    except KeyboardInterrupt:
        # Out application
        # Log if the server stopped using ctrl + c
        log(
            'Server stopped via key combination.'
        )

        # Print server stopped message
        print(f'{Fore.LIGHTBLACK_EX}[Pym]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Server stopped via key combination.{Style.RESET_ALL}')

        # Exit
        exit(0)

# Register command and parser
register(
    name=NAME,
    callable=serve,
    parser=subparsers.add_parser(NAME, help='Create simple server.')
)

# Read this help
parsers[NAME].add_argument(
    '--host',
    '-H',
    required=False,
    type=str,
    default=config.SERVER['local']['host'],
    help=f"[Server] Server host. Default ('{config.SERVER['local']['host']}')."
)

# Read this help
parsers[NAME].add_argument(
    '--port',
    '-p',
    required=False,
    type=int,
    default=config.SERVER['local']['port'],
    help=f"[Server] Server port. Default ({config.SERVER['local']['port']})."
)

# Read this help
parsers[NAME].add_argument(
    '--tree',
    '-t',
    required=False,
    type=str,
    default=config.SERVER['start-folder'],
    help=f"[Server] Server root path. Default ('{config.SERVER['start-folder']}')."
)

# Read this help
parsers[NAME].add_argument(
    '--index',
    '-i',
    required=False,
    type=str,
    default=config.SERVER['start-point'],
    help=f"[Server] Index file within the server's root path. Default ('{config.SERVER['start-point']}')."
)

# Read this help
parsers[NAME].add_argument(
    '--logs-path',
    '-lh',
    required=False,
    type=str,
    default=config.SERVER['logs-file'],
    help=f"[Server] Logs file path. Default ('{config.SERVER['logs-file']}')."
)

# -- FLAG
# Read this help
parsers[NAME].add_argument(
    '--logs',
    default=config.SERVER['logs'],
    action=argparse.BooleanOptionalAction,
    help=f"[Server] Flag to enable/disable logs in file. Actual ({config.SERVER['logs']})."
)

# -- FLAG
# Read this help
parsers[NAME].add_argument(
    '--folder-searching',
    action=argparse.BooleanOptionalAction,
    default=config.SERVER['use-folder-searching'],
    help=f"[Server] Flag to enable/disable file search by URL on the server. Actual ({config.SERVER['use-folder-searching']})."
)