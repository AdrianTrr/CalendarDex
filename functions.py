#Función para guardar en ficheros.
from pathlib import Path
import requests
def writeFile(month, day ,text):
    folder = Path("data")
    fileMonth= month+".txt"
    
    file = folder / fileMonth

    folder.mkdir(parents=True, exist_ok=True)

    day_str=str(day).zfill(2)
    month_index=str(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"].index(month)+ 1).zfill(2)

    entry_id = f"id{day_str}{month_index}"

    # Leer contenido si existe
    if file.exists():
        content = file.read_text(encoding="utf-8").split("\n")
    else:
        content = []

    new_lines = [] # Array que almacena el contenido actualizado
    skip = False # Saltos de lineas antiguas
    replaced = False # Indica si se ha encontrado el entry_id

    for line in content:
        if line.strip() == entry_id:
            skip = True
            replaced = True
            new_lines.append(entry_id)
            new_lines.extend(text.strip().split("\n"))
        elif skip and line.strip() != "" and not line.strip().count("/") == 1:
            continue
        else:
            if skip and (line.strip()== "" or line.strip().count("/")==1):
                skip=False
            new_lines.append(line)

    if not replaced:
        if new_lines and new_lines[-1] != "":
            new_lines.append("")
        new_lines.append(entry_id)
        new_lines.extend(text.strip().split("\n"))
    file.write_text("\n".join(new_lines).strip()+ "\n", encoding="utf-8")
    
    # with file.open("w") as f:
    #     f.write(text)
    # f.close

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