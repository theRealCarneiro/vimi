from alsa_midi import SequencerClient, READ_PORT, PortType, NoteOnEvent, ControlChangeEvent


class Device:
    def __init__(self):

        self.client = SequencerClient("Vimi")
        self.port = self.client.create_port("Vimi midi 0",
                                            caps=READ_PORT,
                                            type=PortType.MIDI_GENERIC |
                                            PortType.MIDI_GM |
                                            PortType.SYNTHESIZER)

    def send_note(self, note):
        event = NoteOnEvent(note)
        self.client.event_output(event, port=self.port)
        print(event)
        self.client.drain_output()

    def send_control(self, param, control):
        event = ControlChangeEvent(channel=0, param=param, value=int(control))
        self.client.event_output(event, port=self.port)
        print(event)
        self.client.drain_output()
