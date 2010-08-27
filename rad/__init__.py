from os.path import abspath, dirname, join
from rad.colorers import Colorer

INSTALL = abspath(dirname(__file__))
SAMPLE = join(INSTALL, 'sample.yaml')

__all__ = ['colorers']

