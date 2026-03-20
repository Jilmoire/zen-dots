import os
from gi.repository import GLib
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button

class batteryWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.icon_label = Label(label="󰁹")
        self.text_label = Label(label="100%")
        
        self.button = Button(
            child=Box(children=[self.icon_label, self.text_label], spacing=4)
        )
        self.add(self.button)
        self.update_battery()
        GLib.timeout_add_seconds(15, self.update_battery)
        
    def update_battery(self):
        try:
            # Battery files
            with open("/sys/class/power_supply/BAT0/capacity", "r") as f:
                capacity = int(f.read().strip())
            with open("/sys/class/power_supply/BAT0/status", "r") as f:
                status = f.read().strip()
            
            self.text_label.set_label(f"{capacity}%")
            
            # Change icon on charging status and percentage
            if status == "Charging":
                self.icon_label.set_label("󰂄")
            else:
                if capacity > 90: self.icon_label.set_label("󰁹")
                elif capacity > 70: self.icon_label.set_label("󰂀")
                elif capacity > 40: self.icon_label.set_label("󰁾")
                elif capacity > 20: self.icon_label.set_label("󰁼")
                else: self.icon_label.set_label("󰂃")
                
        except FileNotFoundError:
            # If no battery
            self.text_label.set_label("AC")
            self.icon_label.set_label("󰚥")
            
        return True # Loop