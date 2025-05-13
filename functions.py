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
    
    from pathlib import Path
    import json

    file = Path("data")/"data.json"

    month = month.lower()
    day_str = str(day)

    if file.exists():
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(month, {}).get(day_str,{}).get("text", "")
    
    return ""

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