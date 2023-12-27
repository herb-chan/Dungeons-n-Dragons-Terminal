from textual.widgets import Button
from textual import events

class LockInButton(Button):
    def __init__(
        self,
        bottombar,
        label="🔒",
        variant="warning",
        *,
        name="+1",
        classes="lock_in",
        disabled=False
    ):
        super().__init__(label=label, variant=variant, name=name, classes=classes, disabled=disabled)
        self.bottombar = bottombar
        
    def on_click(self, event: events.Click) -> None:
        self.bottombar.increase_progress()