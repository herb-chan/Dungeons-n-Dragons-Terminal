from textual import on
from textual.app import ComposeResult
from textual.widgets import Label, TabPane, Select, Footer, Markdown
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
    ("Halfling", "Halfling"),
    ("Human", "Human"),
    ("Tiefling", "Tiefling"),
]

INTRODUCTION = """
Welcome, brave adventurer, to a world of limitless possibilities, a realm where power is yours for the taking, and destiny is in your hands. Your journey begins here, and the first step is to choose your class.

Each class is unique, offering its own set of skills, abilities, and traits that will shape your adventure. Will you be a valiant knight, wielding your sword with honor and courage? Or perhaps a cunning rogue, using stealth and trickery to overcome your foes? Maybe you see yourself as a wise wizard, harnessing the arcane forces to bend reality to your will?

The choice is yours, and each decision will pave the way for your unique story. Remember, there is no right or wrong choice, only different paths on the road to glory.

Choose wisely, for the path you set upon will define your journey, your challenges, and your ultimate destiny. Good luck, adventurer, and may fortune favor the bold!
"""

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
        self.current_race = Markdown("# Please select your race before you continue.", classes="selected_race_title")
        self.completion_status = None
        self.race_info = RaceTabInformations()

    def compose(self) -> ComposeResult:
        yield self.current_race
        yield Markdown(INTRODUCTION, classes="race_introduction")
        yield Select(prompt="Select a race", options=RACES, name="race_select", classes="race_select")
        yield self.race_info
        
    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed) -> None:
        selected_race = event.value 
        if isinstance(selected_race, NoSelection):
            self.current_race.update("# Please select your race.")
            self.race_info.update_race(selected_race)
            if self.completion_status is not None:
                self.bottombar.increase_progress(-1)
                self.completion_status = None
        else:
            self.current_race.update(f"# Selected race: {selected_race}")
            self.race_info.update_race(selected_race)
            self.notify("You can now check all the important informations about it on the right. If you believe that's the race you wanna go with, you can now continue and take a look at the Class tab.", title=f"Successfully selected {selected_race} race.", timeout=5)
            if self.completion_status is None:
                self.bottombar.increase_progress(1)
                self.completion_status = "Done"
