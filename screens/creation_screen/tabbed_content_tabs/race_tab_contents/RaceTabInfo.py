from textual.app import ComposeResult
from textual.widgets import Label
from textual.widget import Widget
from textual.containers import Center

class RaceTabInformations(Widget):    
    def compose(self) -> ComposeResult:
        with Center():
            yield Label("Informations")