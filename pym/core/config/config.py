import json
import re
from pym.core.utils import source

suffix = '.pym'
"""
Pym file suffix.
"""

pysxSuffix = '.pysx'
"""
PYSX Python sintax file suffix.
"""

encoding = 'utf-8'
"""
Encoding used to read config JSON file.
"""

# One-file source
path = source('config.json', __file__)
"""
Config JSON file path.
"""

CONFIG = json.loads(open(path, encoding=encoding).read())
"""
Config JSON data.
"""

PATTERN = re.compile(CONFIG['language']['re-pattern'], re.S | re.M)
"Tag pattern."

INCLUDE = re.compile(CONFIG['language']['include-pattern'], re.S | re.M)
"Include pattern."

COMMONS = {
    'white-lines': re.compile(CONFIG['common-patterns']['white-lines'])
}
"""
Dictionary with common patterns used in the proccessor.
"""

EVALP = re.compile(CONFIG['language']['eval-one-line'], re.S | re.M)
"Pattern to eval one line and echo the output."

PYSX = re.compile(CONFIG['language']['pysx-pattern'])
"Pattern to envolve HTML Tags."