from textual import on
from textual.app import ComposeResult
from textual.widgets import Label, TabPane, Select, Footer
from textual.widgets._select import NoSelection
from textual.containers import Center

from screens.creation_screen.tabbed_content_tabs.race_tab_contents.RaceTabInfo import RaceTabInformations

RACES = [
    ("Aarakocra", "Aarakocra"),
    ("Dragonborn", "Dragonborn"),
    ("Dwarf", "Dwarf"),
    ("Elf", "Elf"),
    ("Genasi", "Genasi"),
    ("Gnome", "Gnome"),
    ("Goliath", "Goliath"),
    ("Half-Elh", "Half-Elh"),
    ("Half-Orc", "Half-Orc"),
    ("Halfling", "Halfling"),
    ("Human", "Human"),
    ("Tiefling", "Tiefling"),
    ("Variamt Aasimar", "Variamt Aasimar")
]

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
        self.current_race = Label("Please select your race before you continue.")
        self.completion_status = None

    def compose(self) -> ComposeResult:
        with Center():
            yield self.current_race
        yield Select(prompt="Select a race", options=RACES, name="race_select", classes="race_select")
        yield RaceTabInformations()
        
    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed) -> None:
        selected_race = event.value 
        if isinstance(selected_race, NoSelection):
            self.current_race.update("Please select your race.")
            if self.completion_status is not None:
                self.bottombar.increase_progress(-1)
                self.completion_status = None
        else:
            self.current_race.update(f"Selected race: {selected_race}")
            if self.completion_status is None:
                self.bottombar.increase_progress(1)
                self.completion_status = "Done"