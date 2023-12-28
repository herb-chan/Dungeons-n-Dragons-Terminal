from textual.app import ComposeResult
from textual.widgets import Label, TabPane

from screens.creation_screen.tabbed_content_tabs.LockInButton import LockInButton

class RaceTabPane(TabPane):
    def __init__(
        self, 
        bottombar,
        title="Race", 
        id="race", 
        **kwargs,
    ):
        super().__init__(title, id=id, **kwargs)
        self.bottombar = bottombar

    def compose(self) -> ComposeResult:
        yield Label("Race Content")
        yield LockInButton(self.bottombar)