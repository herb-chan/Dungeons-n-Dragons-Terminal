from textual.app import ComposeResult
from textual.widgets import Label
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
        self.selected_race_title = Label("Please select your race.", classes="selected_race_title")
        self.selected_race_name = Label(classes="selected_race_name")
        self.selected_race_description = Label(classes="selected_race_description")
        self.selected_race_age = Label(classes="selected_race_age") 
        self.selected_race_alignment = Label(classes="selected_race_alignment") 
        self.selected_race_size = Label(classes="selected_race_size")
        self.selected_race_speed = Label(classes="selected_race_speed") 
        self.selected_race_languages = Label(classes="selected_race_languages")
        self.selected_race_traits = Label(classes="selected_race_traits")
    
    def compose(self) -> ComposeResult:
        with Center():
            yield self.selected_race_title
        yield self.selected_race_name
        yield self.selected_race_description
        yield self.selected_race_age
        yield self.selected_race_alignment 
        yield self.selected_race_size
        yield self.selected_race_speed
        yield self.selected_race_languages 
        yield self.selected_race_traits
                
    def update_race(self, selected_race):
        self.selected_race = selected_race
        if isinstance(selected_race, NoSelection):
            self.selected_race_title.update("Please select your race.")
            self.selected_race_name.update()
            self.selected_race_description.update()
            self.selected_race_age.update()
            self.selected_race_alignment.update()
            self.selected_race_size.update()
            self.selected_race_speed.update()
            self.selected_race_languages.update()
            self.selected_race_traits.update()
        else:
            traits = ', '.join(self.data[self.selected_race]['Racial Traits'])
            self.selected_race_title.update(f"Showing informations for {self.data[self.selected_race]['Name']}.")
            self.selected_race_name.update(f"Name: {self.data[self.selected_race]['Name']}")
            self.selected_race_description.update(f"Description: {self.data[self.selected_race]['Description']}")
            self.selected_race_age.update(f"Age: {self.data[self.selected_race]['Age']}")
            self.selected_race_alignment.update(f"Alignment: {self.data[self.selected_race]['Alignment']}")
            self.selected_race_size.update(f"Size: {self.data[self.selected_race]['Size']}")
            self.selected_race_speed.update(f"Speed: {self.data[self.selected_race]['Speed']}")
            self.selected_race_languages.update(f"Languages: {self.data[self.selected_race]['Languages']}")  
            self.selected_race_traits.update(f"Racial Traits: {traits}")