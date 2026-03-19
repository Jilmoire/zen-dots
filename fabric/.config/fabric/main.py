import os
os.environ["GDK_BACKEND"] = "wayland"

import fabric # base package
from fabric import Application
from fabric.utils import set_stylesheet_from_file

from modules import StatusBar# , ControlCenter, NotificationCenter

if __name__ == "__main__":
    # initialize components
    bar = StatusBar()
    #control_center = ControlCenter()
    #notif_center = NotificationCenter()
    app = Application("my-desktop", bar)#, control_center, notif_center)

    css_file = os.path.join(os.path.dirname(__file__), "style.css")
    set_stylesheet_from_file(css_file)
    
    # 3. Start the engine
    app.run()