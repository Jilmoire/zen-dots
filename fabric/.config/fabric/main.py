import os
os.environ["GDK_BACKEND"] = "wayland"

import fabric # importing the base package
from fabric import Application

from modules import StatusBar# , ControlCenter, NotificationCenter

if __name__ == "__main__":
    # 1. Initialize all your modular widgets
    bar = StatusBar()
    #control_center = ControlCenter()
    #notif_center = NotificationCenter()

    # 2. Pass them ALL into the Fabric Application
    # The Application class will handle rendering all of them simultaneously
    app = Application("my-desktop", bar)#, control_center, notif_center)
    
    # 3. Start the engine
    app.run()