from pym.server import VERSION as S
from pym.core import VERSION as C
from pym.commands import register, subparsers

NAME = 'version'
"Command name."

# Function to print pym modules version
def version(_):
    # Version text
    text = f'Pym Core Version: {C}. Pym Server Version: {S}.'
    print(text)

# Register command and parser
register(
    name=NAME,
    callable=version,
    parser=subparsers.add_parser(NAME, help='Show Pym version.')
)