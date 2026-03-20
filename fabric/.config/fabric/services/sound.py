import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

import fabric # base package

from fabric import Application
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.label import Label
from fabric.audio.service import Audio

class audioManager(Box):
    def __init__(self, **kwargs):
        # Initialization
        super().__init__(**kwargs)
        self.audio = Audio()

        self.icon_label = Label(label="󰕾") 
        self.vol_label = Label(label="100%")
        
        self.button = Button(
            child=Box(
                children=[
                    self.icon_label, 
                    self.vol_label
                    ], 
                spacing=4
                ),
            on_clicked=self.toggle_mute,
        )
        self.button.add_events(Gdk.EventMask.SCROLL_MASK)
        self.button.connect("scroll-event", self.scroll_volume)
        self.add(self.button)

        if self.audio.speaker:
            self.setup_signals()
        else:
            self.audio.connect("notify::speaker", self.setup_signals)

    def setup_signals(self, *args):
        if self.audio.speaker:
            self.audio.speaker.connect("notify::volume", self.update_ui)
            self.audio.speaker.connect("notify::muted", self.update_ui)
            self.update_ui()

    def toggle_mute(self, *args):
        if self.audio.speaker:
            self.audio.speaker.muted = not self.audio.speaker.muted
        else:
            self.vol_label.set_label("NO SPKR")
            self.icon_label.set_label("⚠")

    def scroll_volume(self, widget, event, *args):
        if not self.audio.speaker:
            self.vol_label.set_label("NO SPKR")
            self.icon_label.set_label("⚠")
            return False
            
        step = 5        
        # Standard scrolling
        if event.direction == Gdk.ScrollDirection.UP:
            self.audio.speaker.volume = min(100.0, self.audio.speaker.volume + step)
        elif event.direction == Gdk.ScrollDirection.DOWN:
            self.audio.speaker.volume = max(0.0, self.audio.speaker.volume - step)
            
        # Touchpad
        elif event.direction == Gdk.ScrollDirection.SMOOTH: 
            _, delta_x, delta_y = event.get_scroll_deltas()    
            if delta_y < 0: 
                self.audio.speaker.volume = min(100.0, self.audio.speaker.volume + step)
            elif delta_y > 0: 
                self.audio.speaker.volume = max(0.0, self.audio.speaker.volume - step)

        return True

    def update_ui(self, *args):
        if not self.audio.speaker:
            return
            
        vol = round(self.audio.speaker.volume)
        is_muted = self.audio.speaker.muted

        if is_muted:
            self.icon_label.set_label("󰖁")
            self.vol_label.set_label("Muted")
        else:
            self.icon_label.set_label("󰕾")
            self.vol_label.set_label(f"{vol}%")

if __name__ == "__main__":

    sound = audioManager()
    app = Application("sound", sound)
    app.run()

    