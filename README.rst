A super easy console highlighter. Text goes in, color comes out. rad can be
used to process the output of commands, or to highlight single files.

How it works
------------

rad will read the file given with ``--file/-f``, or stdin if omitted.

Highlighting is specified with re-usable colorer files. Colorer files are
written in `YAML <http://yaml.org/>`_. They contain a collection of rules like
this::

    "regex":
        fore: green
        back: black
        style: normal

or this::

    regex: {fore: red, back: white, style: bright}

and are stored in ``~/.rad/`` by default. The simplest way to use rad is to give
it the names of one or more colorers, like so::

    $ echo "this is a test" | rad colorer1 colorer2

and all rules in the colorers ``~/.rad/colorer1.yaml`` and ``~/.rad/colorer2.yaml``
will be applied to the input text in order!

rad can also make these files for you interactively, using the ``--new/-n`` option::

    $ rad -n
    Colorer name for this rule: logs
    Pattern to match: ERROR
    Foreground color [white]: red
    Background color [black]: 
    Style [bright]: 

    $ tail -f log.txt | rad logs

Colorer files will be appended to, so you can quickly build a colorer with
a bunch of rules by running this a few times.

Roadmap
-------

I plan on supporting the following in future releases of rad, while trying to
keep the usage and syntax super-simple at the same time:

* Multi-line highlighting, using start and stop regexes (e.g. highlight between HTML script tags or in tracebacks)
* Support for syntax highlighting using Pygments by giving a lexer/formatter for a multi-line rule
* Support for 256 colors (using Fabulous...?)
* Other awesome stuff depending on how people want to use it

