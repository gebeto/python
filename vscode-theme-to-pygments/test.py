from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalTrueColorFormatter

from brogrammer_plus import BrogrammerPlusStyle

from sys import argv

print(highlight(open(argv[1]).read(), PythonLexer(), TerminalTrueColorFormatter(style=BrogrammerPlusStyle)))