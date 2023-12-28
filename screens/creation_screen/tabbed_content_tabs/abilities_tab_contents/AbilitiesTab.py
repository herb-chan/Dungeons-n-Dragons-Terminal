from textual.app import ComposeResult
from textual.widgets import Label, TabPane

class AbilitiesTabPane(TabPane):
    def __init__(
        self, 
        title="Abilities", 
        id="abilities", 
        **kwargs
    ):
        super().__init__(title, id=id, **kwargs)

    def compose(self) -> ComposeResult:
        yield Label("Abilities Content")