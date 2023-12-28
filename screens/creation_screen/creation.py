from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, TabbedContent, TabPane

from screens.creation_screen.tabbed_content_tabs.LockInButton import LockInButton
from screens.creation_screen.tabbed_content_tabs.BottomBar import Bottombar

from screens.creation_screen.tabbed_content_tabs.race_tab_contents.RaceTab import RaceTabPane
from screens.creation_screen.tabbed_content_tabs.class_tab_contents.ClassTab import ClassTabPane
from screens.creation_screen.tabbed_content_tabs.abilities_tab_contents.AbilitiesTab import AbilitiesTabPane
from screens.creation_screen.tabbed_content_tabs.equipment_tab_contents.EquipmentTab import EquipmentTabPane
from screens.creation_screen.tabbed_content_tabs.showcase_tab_contents.ShowcaseTab import ShowcaseTabPane

bottombar = Bottombar()

TABS = [
    "Race",
    "Class",
    "Abilities",
    "Equipment",
    "Showcase"
]

class CreationScreen(Screen):
    CSS_PATH = "creation.tcss"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield bottombar
        with TabbedContent(initial="race", classes="Tabs", disabled=False):
            yield RaceTabPane(bottombar)
            yield ClassTabPane()
            yield AbilitiesTabPane()
            yield EquipmentTabPane()
            yield ShowcaseTabPane()