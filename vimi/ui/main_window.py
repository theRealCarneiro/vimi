import os

from vimi.settings import GLADEFILE
from vimi.ui.strip import Strip
from vimi.midi.device import Device

from gi import require_version as gi_require_version
gi_require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.midi = Device()
        self.builder.add_from_file(os.path.join(GLADEFILE, 'main_window.glade'))

        self.window = self.builder.get_object('main_window')
        self.strip_box = self.builder.get_object('strip_box')
        self.window.connect('delete_event', self.delete_event)
        self.builder.connect_signals(self.window)

        play = self.builder.get_object('play')
        play.connect('pressed', self.button_press, 1)

        stop = self.builder.get_object('stop')
        stop.connect('pressed', self.button_press, 2)

        rec = self.builder.get_object('rec')
        rec.connect('pressed', self.button_press, 3)

        prev = self.builder.get_object('prev')
        prev.connect('pressed', self.button_press, 4)

        next = self.builder.get_object('next')
        next.connect('pressed', self.button_press, 5)

        next_track = self.builder.get_object('next_track')
        next_track.connect('pressed', self.button_press, 6)

        prev_track = self.builder.get_object('prev_track')
        prev_track.connect('pressed', self.button_press, 7)

        cycle = self.builder.get_object('cycle')
        cycle.connect('pressed', self.button_press, 8)

        set = self.builder.get_object('set')
        set.connect('pressed', self.button_press, 9)

        next_mark = self.builder.get_object('next_mark')
        next_mark.connect('pressed', self.button_press, 10)

        prev_mark = self.builder.get_object('prev_mark')
        prev_mark.connect('pressed', self.button_press, 11)

        self.create_device()

        self.window.show_all()

    def create_device(self):
        for i in range(3):
            strip = Strip(i)
            strip.vol.connect('value-changed', self.adjust_change, strip.vol_control)
            strip.fx.connect('value-changed', self.adjust_change, strip.fx_control)
            strip.mute.connect('pressed', self.button_press, strip.mute_note)
            strip.solo.connect('pressed', self.button_press, strip.solo_note)
            strip.rec.connect('pressed', self.button_press, strip.rec_note)

            self.strip_box.pack_start(strip, True, True, 0)

    def button_press(self, button, note):
        self.midi.send_note(note)

    def adjust_change(self, adjust, param):
        value = adjust.get_value()
        self.midi.send_control(param, value)

    def delete_event(self, widget=None, event=None):
        Gtk.main_quit()
