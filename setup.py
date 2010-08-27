__author__="Rob O'Dwyer"

from setuptools import setup,find_packages
from os.path import abspath, dirname, join

PROJECT_DIR = abspath(dirname(__file__))

setup (
    name = 'rad',
    version = '0.1',
    packages = find_packages(),
    zip_safe = True,

    install_requires=['pyyaml', 'plac', 'colorama'],

    author = 'Rob O\'Dwyer',
    author_email = 'odwyerrob@gmail.com',

    url = 'http://github.com/robbles/rad',
    license = 'MIT',
    description = 'A super easy console highlighter. Text goes in, color comes out.',
    long_description = open(join(PROJECT_DIR, 'README')).read(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.1',
        'Natural Language :: English',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: Text Processing',
        'Topic :: System :: Shells',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
        'Topic :: System :: Systems Administration',
    ],

    entry_points = {
        'console_scripts': [
            'rad = rad.cmd:main',
        ],
        'gui_scripts': []
    }
)
