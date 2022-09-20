import os


__version__ = '0.1'

# show/hide debug messages
DEBUG = True

HOME = os.getenv('HOME', os.getenv('USERPROFILE'))

USER = os.getenv('USER')
APP_DIR = os.path.dirname(os.path.realpath(__file__))
XDG_CONFIG_HOME = os.getenv('XDG_CONFIG_HOME', f'/home/{USER}/.config')
CONFIG_DIR = os.path.join(XDG_CONFIG_HOME, 'vimi')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
ORIG_CONFIG_FILE = os.path.join(APP_DIR, 'config.json')
GLADEFILE = os.path.join(APP_DIR, 'ui/glade')
