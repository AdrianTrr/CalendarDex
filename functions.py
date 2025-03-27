#Función para guardar en ficheros.
from pathlib import Path
def writeFile(month, text):
    folder = Path("months")
    fileMonth= month+".txt"
    
    file = folder / fileMonth

    folder.mkdir(parents=True, exist_ok=True)

    with file.open("w") as f:
        f.write(text)
    f.close

