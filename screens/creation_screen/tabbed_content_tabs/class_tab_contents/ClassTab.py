from textual.app import ComposeResult
from textual.widgets import Label, TabPane

class ClassTabPane(TabPane):
    def __init__(
        self, 
        title="Class", 
        id="class", 
        **kwargs
    ):
        super().__init__(title, id=id, **kwargs)

    def compose(self) -> ComposeResult:
        yield Label("Class Content")