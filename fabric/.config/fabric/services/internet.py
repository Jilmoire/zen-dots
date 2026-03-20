import subprocess
from gi.repository import GLib
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button

class wifiWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.icon_label = Label(label="󰤨") 
        self.text_label = Label(label="Disconnected")
        
        self.button = Button(
            child=Box(children=[self.icon_label, self.text_label], spacing=4)
        )
        self.add(self.button)
        
        self.update_wifi()
        GLib.timeout_add_seconds(10, self.update_wifi)
        
    def update_wifi(self):
        try:
            cmd = "nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d: -f2"
            output = subprocess.check_output(cmd, shell=True, text=True).strip()
            
            if output: # check for connection. if connected, update the icon the the network name.
                self.icon_label.set_label("󰤨")
                self.text_label.set_label(output)
            else:
                self.icon_label.set_label("󰤭")
                self.text_label.set_label("Disconnected")
        except Exception:
            self.icon_label.set_label("⚠")
            self.text_label.set_label("Network Error")
            
        return True