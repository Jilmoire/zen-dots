from ignis.services.notifications import NotificationService
from ignis.services.niri import NiriService
from ignis.widgets import Widget


niri = NiriService.get_default()
notifications = NotificationService.get_default()


class Workspaces(Widget.Box):
    def __init__(self):
        super().__init__()
        niri.connect("notify::workspaces", self.update)
        niri.connect("notify::focused-workspace", self.update)
        
        self.update()

    def update(self, *args):
        buttons = []
        for workspace in niri.workspaces:
            icon = "●" if workspace.is_active else "○"
            button = Widget.Button(
                child = Widget.Label(label=icon),
                on_click=lambda _, w = workspace: w.switch_to(),
            )
            buttons.append(button)
        
        self.child = buttons

class NotificationMenu(Widget.RevealerWindow):
    def __init__(self):
        self.notif_menu = Widget.Button(
            child = Widget.Label(label="🔔"),
            on_click=lambda _: self.toggle_menu(),
        )
        notifContent = Widget.Box(
                            vertical=True,
                            child=[
                                Widget.Label(label="Notifications"),
                                Widget.Separator(orientation="horizontal"),
                                Widget.Label(label="No new messages"),
                            ],
                        )
        revealer = Widget.Revealer(
            transition_type = "slide_up",
            transition_duration = 300,
            reveal_child = True,
            child = notifContent
        )
        box = Widget.Box(child = [revealer])
        super().__init__(
            namespace = "notification-menu",
            visible = False,
            child = box,
            anchor = ["left", "bottom"],
            revealer = revealer
        )
        self.notifContent = notifContent
        self.revealer = revealer

    def toggle_menu(self):
        self.visible = not self.visible

notif_menu = NotificationMenu()

def left():
    return Widget.Box(
        spacing = 10,
        child=[
            notif_menu.notif_menu,
            Workspaces()
        ]
    )