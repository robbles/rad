"""
A simple console text highlighter. rad can be used to process the output of
commands, or to process multiple files.

Highlighting can be specified at the command line with flags, or with re-usable
colorer files. Colorer files are in YAML, look like this:

"regex":
    fore: green
    back: black
    style: normal

and are stored in "~/.rad/". The simplest way to use rad is to give it the names
of one or more colorers, like so:

$ echo "this is a test" | rad colorer1 colorer2

and all rules in the colorers "~/.rad/colorer1.yaml" and "~/.rad/colorer2.yaml"
will be applied to the input text in order!

rad can also make these files for you interactively, using the --new/-n option.

"""

from os.path import abspath, dirname, join, expanduser

INSTALL = abspath(dirname(__file__))
SAMPLE = join(INSTALL, 'sample.yaml')
CONFIG = expanduser('~/.rad')

# TODO: customize this
#__all__ = ['colorers', ]

