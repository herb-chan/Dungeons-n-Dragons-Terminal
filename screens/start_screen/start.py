from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Button
from textual.widget import Widget
from textual import events

class NewGame(Button):
    def __init__(
        self,
        label="New Game",
        variant="success",
        *,
        name="New Game",
        classes="new_game",
        disabled=False
    ):
        super().__init__(label=label, variant=variant, name=name, classes=classes, disabled=disabled)
        
    def on_click(self, event: events.Click) -> None:
        self.app.switch_mode("creation")
        
class LoadSave(Button):
    def __init__(
        self,
        label="Load Save",
        variant="warning",
        *,
        name="Load Save",
        classes="load_save",
        disabled=False
    ):
        super().__init__(label=label, variant=variant, name=name, classes=classes, disabled=disabled)
        
class Quit(Button):
    def __init__(
        self,
        label="Quit",
        variant="error",
        *,
        name="Quit",
        classes="quit",
        disabled=False
    ):
        super().__init__(label=label, variant=variant, name=name, classes=classes, disabled=disabled)
        
    def on_click(self, event: events.Click) -> None:
        self.app.exit()
        
class Support(Button):
    def __init__(
        self,
        label="Support",
        variant="primary",
        *,
        name="Support",
        classes="support",
        disabled=False
    ):
        super().__init__(label=label, variant=variant, name=name, classes=classes, disabled=disabled)
        
class Options(Widget):    
    def compose(self) -> ComposeResult:
        yield NewGame()
        yield LoadSave()
        yield Quit()
        yield Support()

class StartScreen(Screen):
    CSS_PATH = "start.tcss"
    
    def compose(self) -> ComposeResult:
        yield Options()