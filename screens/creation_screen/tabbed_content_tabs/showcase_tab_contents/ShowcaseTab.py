from textual.app import ComposeResult
from textual.widgets import Label, TabPane

class ShowcaseTabPane(TabPane):
    def __init__(
        self, 
        title="Showcase", 
        id="showcase", 
        **kwargs
    ):
        super().__init__(title, id=id, **kwargs)

    def compose(self) -> ComposeResult:
        yield Label("Showcase Content")