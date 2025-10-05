"""Este archivo contiene una función que escribe texto en un archivo
y devuelve cuántos caracteres fueron escritos."""

def write_file(filename="", text=""):
    """write file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
