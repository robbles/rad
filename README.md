A super easy console highlighter. Text goes in, color comes out. rad can be
used to process the output of commands, or to process multiple files.

How it works
------------
rad will read the file given with `--file/-f`, or stdin if omitted.

Highlighting is specified with re-usable colorer files. Colorer files are in
YAML, contain a collection of rules like this:

    "regex":
        fore: green
        back: black
        style: normal

or this:

    regex: {fore: red, back: white, style: bright}

and are stored in "~/.rad/". The simplest way to use rad is to give it the names
of one or more colorers, like so:

    $ echo "this is a test" | rad colorer1 colorer2

and all rules in the colorers "~/.rad/colorer1.yaml" and "~/.rad/colorer2.yaml"
will be applied to the input text in order!

rad can also make these files for you interactively, using the `--new/-n` option.

Roadmap
-------

I plan on supporting the following in future releases of rad, while trying to
keep the usage and syntax super-simple at the same time:

* Multi-line highlighting, using start and stop regexes (e.g. highlight between <script> ... </script>)
* Support for syntax highlighting using Pygments by giving a lexer/formatter for a multi-line rule
* Support for 256 colors (using Fabulous...?)
* Other awesome stuff depending on how people want to use it

