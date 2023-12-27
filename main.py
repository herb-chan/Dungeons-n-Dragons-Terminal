import json
from rich.console import Console
from rich.table import Table
from rich.progress import Progress  
from rich import box
import inquirer
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def campgain_pick():
    """Picks a campgain from ('assets/dialogues/campgain.json') that the user will be playing 
    
    Currently only one campgain is available, more will come in the future
    
    Returns:
        dict: contains informations about the campgain
    """
    with open('assets/dialogues/campgain.json', 'r') as f:
        data = json.load(f)
        
    return data

def dialogue( data ):
    """Creates a dialogue using 'Console()' class and provided data

    Args:
        data (dict): contains informations about the dialogue
    """
    type = data['type']['value']
    type_colour = data['type']['colour']
    text = data['text']['value']
    text_colour = data['text']['colour'] 
    
    console = Console()
    console.rule(f'[{type_colour}]{type}[white]')
    console.print(f'[{text_colour}]{text}')
    
def start_campgain():
    """Starts a campgain using selected campgain from 'campgain_pick()' function
    """
    selected_class, class_dump = select_class()
    selected_race, class_data = select_race(class_dump)
    
    if selected_class and selected_race:   
        data = campgain_pick()
        dialogue(data)
        
        return class_data

def select_class():
    """Let's user select the class that they will be playing for the rest of the campgain

    Returns:
        string: name of the selected class
    """
    class_question = [ inquirer.List('class',
                                   message='What class will you pick ye adventurer?',
                                   choices=['Berserk', 'Warrior', 'Archer', 'Mage', 'Necromancer', 'Druid'],
                                   carousel=True) ]
    selected_class = inquirer.prompt(class_question)['class']
    
    if selected_class:
        with open('assets/classes/classes.json', 'r') as f:
            data = json.load(f)
            
        class_dump = data[f'{selected_class}']    
            
    return selected_class, class_dump 

def select_race( class_dump ):
    race_question = [ inquirer.List('race',
                                    message='What race will you pick?',
                                    choices=['Human', 'Dwarf', 'Elf', 'Dark Elf', 'Goblin', 'Demon'],
                                    carousel=True) ]
    selected_race = inquirer.prompt(race_question)['race']
    
    file_question = [ inquirer.Text('name', message='Enter your character name') ]
    file_name = inquirer.prompt(file_question)['name']
    
    if selected_race:   
        class_dump['Race'] = selected_race
        
        with open(f'save/{file_name}.json', 'w') as f:
            json.dump(class_dump, f, indent=4)
        
        clear_terminal()
            
    return selected_race, class_dump

def load_campgain():
    """Loads the currently saved character from ('save/'character'.json')
    
    If there aren't any characters saved it guides you into creating a brand new one
    
    Returns:
        dict: contains informations about the character
    """
    saves = [f for f in os.listdir('save') if f.endswith('.json')]
    save = [ inquirer.List('option',
                            message='Select a save',
                            choices=saves,
                            carousel=True) ]
    selected_save = inquirer.prompt(save)['option']
    
    with open(f'save/{selected_save}', 'r') as f:
        data = json.load(f)
            
    if data['Name'] is not None:
        return data
    else:
        with open('assets/dialogues/communiques.json', 'r') as f:
            dialogue_data = json.load(f)
        dialogue(dialogue_data)
        start_choices()
        
def start_choices():
    options = ['Start a new game', 'Load save', 'Exit']
    options_question = [ inquirer.List('option',
                                       message='What will you do next?',
                                       choices=options,
                                       carousel=True) ]
    selected_option = inquirer.prompt(options_question)['option']
    
    if selected_option:
        clear_terminal()
        
        if selected_option == options[0]:
            character_data = start_campgain()
            return character_data
        
        elif selected_option == options[1]:
            character_data = load_campgain()
            return character_data
        
        else:
            exit()
            
class Character:
    def __init__(self, character_data):
        self.class_name = character_data['Name']
        self.race = character_data['Race']
        self.main_stat = character_data['MainStat']
        self.health = {
            "current_value": character_data['Health']['current_value'],
            "maximum_value": character_data['Health']['maximum_value']
        }
        self.strength = {
            "current_value": character_data['Strength']['current_value'],
            "maximum_value": character_data['Strength']['maximum_value']
        }
        self.defence = {
            "current_value": character_data['Defence']['current_value'],
            "maximum_value": character_data['Defence']['maximum_value']
        }
        self.agility = {
            "current_value": character_data['Agility']['current_value'],
            "maximum_value": character_data['Agility']['maximum_value']
        }
        self.intelligence = {
            "current_value": character_data['Intelligence']['current_value'],
            "maximum_value": character_data['Intelligence']['maximum_value']
        }
        self.inventory = character_data['Inventory']
        self.experience = character_data['Experience']
        self.level = character_data['Level']
        self.save_name = character_data['Save_Name']

    def gather( self, loot ):
        self.inventory = {
            k: self.inventory.get(k, 0) + loot.get(k, 0) \
            for k in set (self.inventory | loot)
        }
        self.save_progress('Inventory', self.inventory)
        
    def save_progress( self, json_attribute, attribute ):
        with open(f'save/{self.save_name}.json', 'r') as f:
            data = json.load(f)
            
        data[f'{json_attribute}'] = attribute
        
        with open(f'save/{self.save_name}.json', 'w') as f:
            json.dump(data, f, indent=4)
            
    def sheet( self ):
        table = Table(
            title=f'You\'re playing as [cyan]{self.class_name}[/cyan] class. Your main statistic is [cyan]{self.main_stat}[/cyan].', 
            title_justify='left', 
            title_style='white',
            box=box.MINIMAL, 
            width=75)

        table.add_column('Statistic', justify='center', style='bright_white')
        table.add_column('Current', justify='center', style='cyan')
        table.add_column('Maximum', justify='center', style='magenta')
        table.add_column('Class bonus', justify='center', style='green')
        table.add_column('Items bonus', justify='center', style='bright_yellow')

        table.add_row('Health', f'{self.health["current_value"]}', f'{self.health["maximum_value"]}', "0", "0")
        table.add_row('Strength', f'{self.strength["current_value"]}', f'{self.strength["maximum_value"]}', "0", "0")
        table.add_row('Defence', f'{self.defence["current_value"]}', f'{self.defence["maximum_value"]}', "0", "0")
        table.add_row('Agility', f'{self.agility["current_value"]}', f'{self.agility["maximum_value"]}', "0", "0")
        table.add_row('Intelligence', f'{self.intelligence["current_value"]}', f'{self.intelligence["maximum_value"]}', "0", "0")

        console = Console()
        console.print(table)
        console.print('[[bright_red][bold]![/bold][/bright_red]] Please note that your statistics are dependent on the class you\'ve selected and the items you\'re wearing.\n')
        
        self.show_experience_bar()        
            
    def show_experience_bar( self ):
        experience_needed = 5 * (self.level ^ 2) + (50 * self.level) + 222.5
        
        console = Console()
        console.print(f'You are currently level {self.level} and {experience_needed - self.experience} exp away from the level {self.level + 1}.')
        with Progress() as progress:
            task = progress.add_task("[cyan]Experience...", total=experience_needed, completed=self.experience)
    
def __main__():
   character_data = start_choices()
   character = Character(character_data)
   character.sheet()
#    load_campgain()
    
__main__()