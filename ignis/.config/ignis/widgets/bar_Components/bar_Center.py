import datetime
from ignis.widgets import Widget
from ignis.utils import Utils


def center():

    time = Widget.Label(label=">.<")
    def update_time():
        dt = datetime.datetime.now().strftime("%H:%M - %b %d")
        time.set_label(dt)

    Utils.Poll(timeout=1000, callback=lambda self: update_time())
    update_time()








    return Widget.Box(
        spacing=10,
        child=[
            Widget.Label(label="focused window icon"),
            time
        ]
    )