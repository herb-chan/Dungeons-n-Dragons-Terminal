from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label
from screens.start_screen.start import StartScreen
from screens.creation_screen.creation import CreationScreen

class DnDTerminal(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("t", "toggle_dark", "Toggle dark mode"),
        ]
    
    MODES = {
        "start": StartScreen,
        "creation": CreationScreen
    }
    
    def on_mount(self) -> None:
        self.switch_mode("start")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark 


if __name__ == "__main__":
    app = DnDTerminal()
    app.run()