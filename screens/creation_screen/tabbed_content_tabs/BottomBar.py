from textual.app import ComposeResult
from textual.widgets import Label, ProgressBar
from textual.containers import Center, Middle
from textual.widget import Widget

class Bottombar(Widget):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.progress_bar = ProgressBar(total=4, show_eta=False)

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield Label("Creation progress: ")
                yield self.progress_bar
            
    def increase_progress(self) -> None:
        self.progress_bar.advance(1) 