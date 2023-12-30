from textual.app import ComposeResult
from textual.widgets import Label, Markdown
from textual.widget import Widget
from textual.containers import Center
from textual.widgets._select import NoSelection
import json

class RaceTabInformations(Widget):    
    def __init__(
        self,
        selected_race=None,
        *children,
        name=None,
        id=None,
        classes=None,
        disabled=False
    ):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled, *children)
        
        with open('assets/races/races.json', 'r') as f:
            data = json.load(f)
            
        self.data = data
        self.selected_race = selected_race
        self.selected_race_title = Markdown("# Informations about selected race.", classes="selected_race_title")
        self.selected_race_description = Markdown(classes="selected_race_description")
        self.selected_race_traits = Markdown(classes="selected_race_traits")
    
    def compose(self) -> ComposeResult:
        yield self.selected_race_title
        yield self.selected_race_description
        yield self.selected_race_traits
                
    def update_race(self, selected_race):
        self.selected_race = selected_race
        if isinstance(selected_race, NoSelection):
            self.selected_race_title.update("#  Informations about selected race.")
            self.selected_race_description.update('')
            self.selected_race_traits.update('')
        else:
            traits = """""".join(self.data[self.selected_race]['Racial Traits'])
            self.selected_race_title.update(f"# Informations about {self.data[self.selected_race]['Name']} race.")
            self.selected_race_description.update(f"## Description \n {self.data[self.selected_race]['Description']}")
            self.selected_race_traits.update(f"## Racial Traits {traits}")
            
    def on_mount(self) -> None:
        self.query_one(".selected_race_traits").tooltip = "Racial traits are distinctive physical or behavioral characteristics that are shared by a group of people. In the context of role-playing games like Dungeons & Dragons, racial traits often refer to the inherent abilities, skills, or qualities of a particular race. "