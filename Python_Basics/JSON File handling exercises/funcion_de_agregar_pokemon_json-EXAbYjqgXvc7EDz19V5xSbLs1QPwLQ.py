import json

ruta="C:\\Users\\jmata\\OneDrive\\Desktop\\pokemon.json"

def get_integer(message):

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Error: Enter a valid number")


def get_float(message):

    while True:
        try:
            return float(input(message))

        except ValueError:
            print("Error: Enter a valid number")


def get_text(message):

    while True:

        text = input(message).strip()

        if text == "":
            print("Error: Input cannot be empty")

        elif any(char.isdigit() for char in text):
            print("Error: Numbers are not allowed")

        else:
            return text
    
def get_boolean(message):
    while True:
        response = input(message).lower()

        if response in ["yes", "y"]:
            return True

        elif response in ["no", "n"]:
            return False

        else:
            print("Error: Please enter 'yes' or 'no'")

def getpokemon_data():
        new_pokemon = {
        "name": get_text("Name: "),
        "type": get_text("Type: "),
        "level": get_integer("Level: "),
        "weight_kg": get_float("Weight kg: "),
        "is_shiny": get_boolean("Shiny (yes/no): "),
        "held_item": input("Held item (leave empty if none): ") or None,
        "skills": [],
        "stats": {}
    }

    
        for i in range(2):

            skill = get_text(f"Skill {i+1}: ")
            new_pokemon["skills"].append(skill)

        
        new_pokemon["stats"] = {
            "hp": get_integer("HP: "),
            "attack": get_integer("Attack: "),
            "defense": get_integer("Defense: "),
            "sp_attack": get_integer("Sp Attack: "),
            "sp_defense": get_integer("Sp Defense: "),
            "speed": get_integer("Speed: ")
        }
        return new_pokemon
    

        
def load_pokemonfile():
    try:

        with open(ruta, "r") as file:
            pokemon = json.load(file)

    except FileNotFoundError:
        pokemon = []

    except json.JSONDecodeError:
        pokemon = []
    return pokemon

def save_pokemon(pokemon):

    try:
        with open(ruta, "w") as file:
            json.dump(pokemon, file, indent=4)

    except IOError:
        print("Error: Could not save the Pokemon data")
        
def add_pokemon():

    new_pokemon = getpokemon_data()
    
    pokemon = load_pokemonfile()
    
    pokemon.append(new_pokemon)
    save_pokemon(pokemon)

    print("Pokemon added successfully")


add_pokemon()
    