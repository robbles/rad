import colorama
import re


class Colorer(object):
    """
    A rule that matches a regular expression, with instructions on how to
    color, format, or otherwise mangle the text it matches.
    """
    def __init__(self, regex, settings):
        self._regex = regex
        self.regex = re.compile(regex)
        self.settings = settings

        self.fore = settings.get('fore', '').upper()
        self.back = settings.get('back', '').upper()
        self.style = settings.get('style', 'normal').upper()

        self.transform = ''.join([
            getattr(colorama.Fore, self.fore, ''),
            getattr(colorama.Back, self.back, ''),
            getattr(colorama.Style, self.style, 'NORMAL')])

        self.reset = ''.join([
            colorama.Fore.RESET, 
            colorama.Back.RESET, 
            colorama.Style.NORMAL])

    def matches(self, line):
        return True if self.regex.search(line) else False

    def color(self, line):
        return self.regex.sub(self.process, line)

    def process(self, match):
        piece = match.group(0)
        return ''.join([self.transform, piece, self.reset])


