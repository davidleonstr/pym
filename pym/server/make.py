from wsgiref.simple_server import make_server

# Function used for WSGI
from pym.server.application import application

# Funtion to write logs in file
from pym.server.utils import log

# Console style
from colorama import Fore, Style

# To get local IP
import socket

# Fnction to make a server
def make(args: dict) -> None:
    # Out application
    # Server start log
    log(
        f"Server started on HOST '{args['host']}' and PORT {args['port']}."
    )

    # Out application
    print(
        f"{Fore.LIGHTBLACK_EX}[Pym]{Style.RESET_ALL} Server started on HOST {Fore.LIGHTGREEN_EX}'{args['host']}'{Style.RESET_ALL} and PORT {Fore.LIGHTBLUE_EX}{args['port']}{Style.RESET_ALL}."
    )

    # Getting local IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = args['host']
    finally:
        s.close()
    
    # Out application
    print(
        f"{Fore.LIGHTBLACK_EX}[Pym]{Style.RESET_ALL} External connections: http://{ip}:{args['port']}/."
    )

    # Out application
    print(
        f"{Fore.LIGHTBLACK_EX}[Pym]{Style.RESET_ALL} Local machine: http://{args['host']}:{args['port']}/."
    )

    httpd = make_server(args['host'], args['port'], application)
    httpd.serve_forever()