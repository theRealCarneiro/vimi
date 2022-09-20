import os
import sys

from vimi.settings import GLADEFILE

from gi import require_version as gi_require_version
gi_require_version('Gtk', '3.0')
from gi.repository import Gtk


class Strip(Gtk.Grid):
    def __init__(self, index):
        builder = Gtk.Builder()
        super(Strip, self).__init__()

        try:
            builder.add_objects_from_file(
                os.path.join(GLADEFILE, 'strip.glade'),
                ['strip', 'vol', 'fx']
            )
        except Exception as ex:
            print(f'Error building strip {index}!\n{ex}')
            sys.exit(1)

        self.grid = builder.get_object('strip')

        self.vol = builder.get_object('vol')
        self.vol_control = (index * 2 + 1)

        self.fx = builder.get_object('fx')
        self.fx_control = (index * 2 + 2)

        self.mute = builder.get_object('mute')
        self.mute_note = (index * 3 + 1) + 11

        self.solo = builder.get_object('solo')
        self.solo_note = (index * 3 + 2) + 11

        self.rec = builder.get_object('rec')
        self.rec_note = (index * 3 + 3) + 11

        self.add(self.grid)
