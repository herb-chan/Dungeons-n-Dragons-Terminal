from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, TabbedContent, TabPane

from screens.creation_screen.tabbed_content_tabs.LockInButton import LockInButton
from screens.creation_screen.tabbed_content_tabs.BottomBar import Bottombar

bottombar = Bottombar()

TABS = [
    "Race",
    "Class",
    "Abilities",
    "Equipment",
    "Showcase"
]

class Tabs(TabbedContent):
    def __init__(
        self,
        initial="race",
        classes="Tabs",
        disabled=False
    ):
        super().__init__(initial=initial, classes=classes, disabled=disabled)

class CreationScreen(Screen):
    CSS_PATH = "creation.tcss"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield bottombar
        
        with TabbedContent(initial="race"):
            with TabPane("Race", id="race"):
                yield LockInButton(bottombar)
                
            with TabPane("Class", id="class"):
                yield Label("Class")
                    
            with TabPane("Abilities", id="Abilities"):
                yield Label("Abilities")
                
            with TabPane("Equipment", id="equipment"):
                yield Label("Equipment")
                
            with TabPane("Showcase", id="showcase"):
                yield Label("Showcase")
        
    def action_show_tab(self, tab: str) -> None:
        self.get_child_by_type(TabbedContent).active = tab