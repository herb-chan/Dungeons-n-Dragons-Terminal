from textual import on
from textual.app import ComposeResult
from textual.widgets import TabPane, Select, Markdown
from textual.widgets._select import NoSelection

from screens.creation_screen.tabbed_content_tabs.class_tab_contents.ClassTabInfo import ClassTabInformations

CLASSES = [
    ("Berserk", "Berserk"),
    ("Warrior", "Warrior"),
    ("Archer", "Archer"),
    ("Mage", "Mage"),
    ("Necromancer", "Necromancer"),
    ("Druid", "Druid"),
]

INTRODUCTION = """
"""

class ClassTabPane(TabPane):
    def __init__(
        self, 
        bottombar,
        title="Class", 
        id="class", 
        **kwargs,
    ):
        super().__init__(title, id=id, **kwargs)
        self.bottombar = bottombar
        self.current_class = Markdown("# Please select your class before you continue.", classes="selected_class_title")
        self.completion_status = None
        self.class_info = ClassTabInformations()

    def compose(self) -> ComposeResult:
        yield self.current_class
        yield Markdown(INTRODUCTION, classes="class_introduction")
        yield Select(prompt="Select a class", options=CLASSES, name="class_select", classes="class_select")
        yield self.class_info
        
    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed) -> None:
        selected_class = event.value 
        if isinstance(selected_class, NoSelection):
            self.current_class.update("# Please select your class.")
            self.class_info.update_class(selected_class)
            if self.completion_status is not None:
                self.bottombar.increase_progress(-1)
                self.completion_status = None
        else:
            self.current_class.update(f"# Selected class: {selected_class}")
            self.class_info.update_class(selected_class)
            self.notify("You can now check all the important informations about it on the right. If you believe that's the class you wanna go with, you can now continue and take a look at the Abilities tab.", title=f"Successfully selected {selected_class} class.", timeout=5)
            if self.completion_status is None:
                self.bottombar.increase_progress(1)
                self.completion_status = "Done"
