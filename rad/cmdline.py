from sys import stdin, stdout, argv
import os
import yaml
import plac
import colorama

from rad import INSTALL, SAMPLE
from rad.rules import Rule, RuleList

@plac.annotations(
config=('Location of colorer files (default ~/.rad)', 'option', 'c', None, None, 'DIR'),
file=('File to process (default stdin)', 'option', 'f', None, None, 'FILE'),
verbose=('Show extra info about colorers and rules being applied', 'flag', 'v'),
new=('Create a new rule', 'flag', 'n'),
listing=('List all rules, ordered by colorer', 'flag', 'l'),
colorers=('List of colorers to apply to the input', 'positional'))
def run(config='~/.rad', file='-', verbose=False, new=False, listing=False, *colorers):
    config = os.path.expanduser(config)

    if file == '-':
        inputfile = stdin
    else:
        inputfile = open(file, 'rU')

    try:
        rules = RuleList(colorers, config_dir=config)
    except (KeyError, OSError) as e:
        print('Error reading colorer files: %s' % e)
        exit(1)

    if verbose:
        from pprint import pprint
        pprint(rules)

    if new:
        rule = rules.create_interactive()
        if verbose:
            print 'created new rule: ' + rule
        exit(0)

    if listing:
        rules.print_listing()
        exit(0)

    colorama.init()

    while 1:
        line = inputfile.readline()

        if not line:
            break
        
        for rule in rules:
            if rule.matches(line):
                line = rule.color(line)

        stdout.write(line)

def main():
    try:
        plac.call(run)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

