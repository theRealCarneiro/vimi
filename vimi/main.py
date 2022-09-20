from vimi.ui.main_window import MainWindow

from gi import require_version as gi_require_version
gi_require_version('Gtk', '3.0')
from gi.repository import Gtk


def main():
    MainWindow()
    Gtk.main()
    return 0
