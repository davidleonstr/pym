import sys
from pym.commands import utilities, parser

def main():
    args = parser.parse_args()

    if not args.utility:
        parser.print_help()
        sys.exit(1)

    if args.utility in utilities:
        utilities[args.utility](args)

if __name__ == '__main__':
    main()