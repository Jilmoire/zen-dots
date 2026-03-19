import fabric # importing the base package
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
            anchor="left bottom right",  # Anchors the bar at the top, stretching from left to right
            exclusivity="auto",  # Reserves space for the bar so it behaves like a normal window
            **kwargs
        )

        leftContainer = Box(
            spacing=10,
            children =[
                Button()
            ]
        )

        centerContainer = Box(
            orientation="h",   # Locks it side-by-side
            spacing=10,
            children=[
                Button(label="Previous"), 
                DateTime(formatters=["%I:%M %p  -  %A, %B %d"]),
                Button(label="Next")
            ]
        )

        rightContainer = Box(
            spacing=10,
            children =[
                Button(),
                Button()
            ]
        )

        barLayout = CenterBox(
            start_children=leftContainer,
            center_children=centerContainer,
            end_children=rightContainer
        )

        self.add(barLayout)

       # self.date_time = DateTime()
       # self.children = CenterBox(center_children=self.date_time)  # Adds the CenterBox with date_time in the center of the bar

if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar", bar)
    app.run()