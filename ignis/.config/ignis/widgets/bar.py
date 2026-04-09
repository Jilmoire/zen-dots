from ignis.widgets import Widget

from .bar_Components.bar_Left import left
from .bar_Components.bar_Center import center
#from .bar_Components.bar_Right import right

class BottomBar(Widget.Window):

    def __init__(self):
        super().__init__(
                namespace="bottom-bar",
                exclusivity="exclusive",
                anchor=["left", "bottom", "right"],
                layer="top",

                child=Widget.CenterBox(  
                    start_widget=left(),
                    center_widget=center(),
                    end_widget=Widget.Label(label="test3")
                ),
        )
