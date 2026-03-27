import widgets

from ignis.widgets import Widget

Widget.Window(
    namespace="bottom-bar",
    exclusivity="exclusive",
    anchor=["left", "bottom", "right"],
    layer="top",

    child=Widget.CenterBox(  
        start_widget=widgets.left(),
        center_widget=widgets.center(),
        end_widget=Widget.Label(label="test3")
    ),
)