import os
import yaml
from . import CONFIG
import colorama
import re


class Rule(object):
    """
    A rule that matches a regular expression, with instructions on how to
    color, format, or otherwise mangle the text it matches.
    """
    def __init__(self, regex, settings):
        self.regex = regex
        self.pattern = re.compile(regex)
        self.settings = settings

        self.fore = settings.get('fore', '').upper()
        self.back = settings.get('back', '').upper()
        self.style = settings.get('style', 'normal').upper()

        self.transform = ''.join([
            getattr(colorama.Fore, self.fore, ''),
            getattr(colorama.Back, self.back, ''),
            getattr(colorama.Style, self.style, '')])

        self.reset = ''.join([
            colorama.Fore.RESET, 
            colorama.Back.RESET, 
            colorama.Style.NORMAL])

    def __repr__(self):
        return 'Rule /%s/ -> fore:%s back:%s style:%s' % (self.regex,
                self.fore, self.back, self.style)

    def matches(self, line):
        return True if self.pattern.search(line) else False

    def color(self, line):
        return self.pattern.sub(self.process, line)

    def process(self, match):
        piece = match.group(0)
        return ''.join([self.transform, piece, self.reset])





class RuleList(list):
    """
    Fetches rules from the default configuration directory (~/.rad/).
    Call get_colorers with a list of names to parse the rules from the files
    with the same name (minus the extension). Rules are returned in the same
    order as the names are given, with the same order as the file's rules.
    """
    def __init__(self, names, config_dir=CONFIG, ext='.yaml'):
        """ 
        Construct a new RuleList that looks in config_dir for colorer files
        that end in ext. 
        """
        self.config_dir = CONFIG
        self.ext = ext

        # If config_dir doesn't exist, try to create it
        if not os.path.exists(config_dir):
            os.mkdir(config_dir)

        # Pre-fetch all the colorer names since they aren't going anywhere
        self.configs = [os.path.join(config_dir, f) 
                        for f in os.listdir(config_dir) 
                        if f.endswith(ext)]

        for rules in self.get_colorers(names):
            self.extend(rules)

    def get_colorers(self, names):
        """ Parse and return rules for colorers by name, in the given order. """
        return [self.get_rules(name) for name in names]

    def get_rules(self, name):
        """ Get all the rules from a given colorer filename """
        # Check if we have a config file for this colorer, and squawk otherwise
        filename = self.name_to_path(name)
        if filename not in self.configs:
            raise KeyError(name)

        # Parse the file
        parsed = yaml.load(open(filename, 'rU'))

        for regex, settings in parsed.items():
            yield Rule(regex, settings)

    def name_to_path(self, name):
        filename = ''.join([name, self.ext])
        path = os.path.join(self.config_dir, filename)
        return path

    def path_to_name(self, path):
        filename = os.path.basename(path)
        name = os.path.splitext(filename)[0]
        return name
            
    def create_interactive(self):
        """ Create a new rule interactively and save it to config_dir. """
        colorer = raw_input('Colorer name for this rule: ')
        regex = raw_input('Pattern to match: ')
        fore = raw_input('Foreground color [white]: ') or 'white'
        back = raw_input('Background color [black]: ') or 'black'
        style = raw_input('Style [bright]: ') or 'bright'
        data = {regex:{'fore':fore, 'back':back, 'style':style}}

        # Parse the rule before saving
        rule = Rule(regex, data[regex])

        # Figure out where to put the damn thing
        filename = self.name_to_path(colorer)

        # Append rule to the new file
        fp = open(filename, 'a')
        yaml.dump(data, fp)

        return rule

    def print_listing(self):
        """ Print out a list of colorers and rules. """
        colorers = [(self.path_to_name(config),
                     self.get_rules(self.path_to_name(config)))
                    for config in self.configs]

        for colorer, rules in colorers:
            print colorer
            print '=' * len(colorer)
            for rule in rules:
                print rule
            print








