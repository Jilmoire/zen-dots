from ignis.services.notifications import NotificationService
from ignis.services.niri import NiriService
from ignis.widgets import Widget


niri = NiriService.get_default()
notifications = NotificationService.get_default()

def left():
    workspaces = Widget.Box(
        spacing=8
    )

    def update_Workspaces(*_):

        buttons = []
        for workspace in niri.workspaces:
            icon = "●" if workspace.is_active else "○"
    
            button = Widget.Button(
                        child=Widget.Label(label=f"{icon}"),
                        on_click=lambda _, w=workspace: w.activate(),
                 )
            buttons.append(button)
        workspaces.child = buttons

    niri.connect("notify::workspaces", update_Workspaces),
    niri.connect("notify::focused-workspace", update_Workspaces)
    
    update_Workspaces()
    return workspaces