from textual.app import ComposeResult
from textual.widgets import Markdown
from textual.widget import Widget
from textual.widgets._select import NoSelection
import json

class ClassTabInformations(Widget):    
    def __init__(
        self,
        selected_class=None,
        *children,
        name=None,
        id=None,
        classes=None,
        disabled=False
    ):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled, *children)
        
        with open('assets/classes/classes.json', 'r') as f:
            data = json.load(f)
            
        self.data = data
        self.selected_class = selected_class
        self.selected_class_title = Markdown("# Informations about selected class.", classes="selected_class_title")
        self.selected_class_description = Markdown(classes="selected_class_description")
        self.selected_class_traits = Markdown(classes="selected_class_traits")
    
    def compose(self) -> ComposeResult:
        yield self.selected_class_title
        yield self.selected_class_description
        yield self.selected_class_traits
                
    def update_class(self, selected_class):
        self.selected_class = selected_class
        if isinstance(selected_class, NoSelection):
            self.selected_class_title.update("#  Informations about selected class.")
            self.selected_class_description.update('')
            self.selected_class_traits.update('')
        else:
            self.selected_class_title.update(f"# Informations about {self.data[self.selected_class]['Name']} class.")
            self.selected_class_description.update(f"## Description \n {self.data[self.selected_class]['Description']}")
            self.selected_class_traits.update(f"## Detailed informations")