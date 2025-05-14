#Función para guardar en ficheros.
from pathlib import Path
import requests
from datetime import datetime
import json

def writeFile(month, day ,text):
    folder = Path("data")
    
    file = folder / "data.json"

    folder.mkdir(parents=True, exist_ok=True)

    data = {}

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    
    month = month.lower()
    day_str = str(day)

    if month not in data:
        data[month] = {}
    
    data[month][day_str] = {"text": text}

    with file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def readFile(day, month):
    file = Path("data")/"data.json"

    month = month.lower()
    day_str = str(day)

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(month, {}).get(day_str,{}).get("text", "")
    
    return ""

def save_pokemon_id(month, day, pokemon_id):
    file = Path("data")/"data.json"
    
    month = month.lower()
    day_str = str(day)

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    
    if month not in data:
        data[month] = {}
    
    if day_str not in data[month]:
        data[month][day_str] = {}

    if "pokemon_id" not in data [month][day_str]:
        data[month][day_str]["pokemon_id"] = pokemon_id

        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def read_pokemon_id(month, day):
    month = month.lower()
    file = Path("data")/"data.json"

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get(month, {}).get(str(day), {}).get("pokemon_id")
                
            except json.JSONDecodeError:
                data = {}
                return None
    return None

# def apiRequest(pokemonId):
#     url='https://pokeapi.co/api/v2/pokemon/'+pokemonId
#     response=requests.get(url)

#     if response.status_code !=200:
#         print("Error:", response.status_code)
#         print(response.text)
#         return None
#     else:
#         data=response.json()
#         pokemon=data['name']
#         return pokemon
    
def get_pokemon_data(pokemonId):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemonId}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.status_code)
        return None, None
    data = response.json()
    name = data['name']
    sprite_url = data['sprites']['front_default']
    return name.capitalize(), sprite_url