#Función para guardar en ficheros.
from pathlib import Path
import requests
def writeFile(month, text):
    folder = Path("months")
    fileMonth= month+".txt"
    
    file = folder / fileMonth

    folder.mkdir(parents=True, exist_ok=True)

    with file.open("w") as f:
        f.write(text)
    f.close

def apiRequest(pokemonId):
    url='https://pokeapi.co/api/v2/pokemon/'+pokemonId
    response=requests.get(url)

    if response.status_code !=200:
        print("Error:", response.status_code)
        print(response.text)
        return None
    else:
        data=response.json()
        pokemon=data['name']
        return pokemon