from textual.app import ComposeResult
from textual.widgets import Label, TabPane

class EquipmentTabPane(TabPane):
    def __init__(
        self, 
        title="Equipment", 
        id="equipment", 
        **kwargs
    ):
        super().__init__(title, id=id, **kwargs)

    def compose(self) -> ComposeResult:
        yield Label("Equipment Content")