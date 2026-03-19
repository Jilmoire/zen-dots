import fabric # base package

from fabric import Application
from fabric.widgets.wayland import WaylandWindow as Window 
from fabric.widgets.datetime import DateTime
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.label import Label


class StatusBar(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top",  # Ensure it stays above other apps
            anchor="left bottom right",  # Anchors the bar at the bottom, stretching from left to right
            exclusivity="auto",  # Reserves space for the bar
            **kwargs
        )

        leftContainer = Box(
            spacing=10,
            children =[
                Button(label="Distro Icon(notif center)"),
                Box(
                    children=[
                        Button(label="●"), # Workspace 1 (Filled circle for "active")
                        Button(label="○"), # Workspace 2 (Empty circle)
                        Button(label="○"), # Workspace 3
                        Button(label="○"), # Workspace 4
                        Button(label="○"), # Workspace 5
                    ]
                ),
                Button(label="music widget")
            ]
        )

        centerContainer = Box(
            spacing=10,
            children=[
                Label(label="focused window icon  · "), 
                DateTime(formatters=["%H:%M - %B %d"])
            ]
        )

        rightContainer = Box(
            spacing=10,
            children=[
                Button(label="tray"),
                Box(
                    children =[
                        Button(label="wifi"),
                        Button(label="sound"),
                        Button(label="battery"),
                    ]
                ),
                Box(
                    children =[
                        Button(label="controlcenter"),
                        Button(label="power")
                    ]
                )
            ]
        )

        barLayout = CenterBox(
            start_children=leftContainer,
            center_children=centerContainer,
            end_children=rightContainer
        )

        self.add(barLayout)

if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar", bar)
    app.run()