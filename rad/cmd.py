from sys import stdin, stdout, argv
import yaml

from rad import Colorer, INSTALL, SAMPLE

#TODO: create parser types for config dir and radfiles list

def run(config : ('Location of .rad files', 'option', 'c') = '~/.rad',
        *radfiles : ('List of rad files to apply to the input', 'positional')):

    print('looking in %s' % config)
    print('radfiles are %s' % (radfiles,))

    radfile = yaml.load(open(SAMPLE))

    colorers = [Colorer(regex, settings) 
            for regex, settings in radfile.items()]

    for c in colorers:
        print('Coloring /%s/ %s/%s' % (c._regex, c.fore, c.back))

    while 1:
        line = stdin.readline()

        if not line:
            break
        
        for c in colorers:

            if c.matches(line):
                line = c.color(line)

        stdout.write(line)

def main():
    try:
        import plac;plac.call(run)
    except KeyboardInterrupt:
        pass

