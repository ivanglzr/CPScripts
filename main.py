import os
import shutil
import string
import sys

def print_usage():
    print("Uso: python gen_contest.py <nombre_carpeta> -n <número_de_archivos> [-t]")
    print(" - <nombre_carpeta>: Carpeta donde se crearán los archivos")
    print(" - -n: Número de archivos a crear (1 a 26)")
    print(" - -t: (opcional) usa template2.cpp en vez de template.cpp")
    sys.exit(1)

# Validar argumentos mínimos
if len(sys.argv) < 4:
    print_usage()

folder_name = sys.argv[1]

# Buscar -n y su valor
if "-n" not in sys.argv:
    print("❌ Falta opción -n")
    print_usage()

try:
    n_index = sys.argv.index("-n") + 1
    n = int(sys.argv[n_index])
    if not (1 <= n <= 26):
        raise ValueError
except (ValueError, IndexError):
    print("❌ Debes indicar un número entero entre 1 y 26 tras -n")
    print_usage()

# Comprobar -t
use_template2 = "-t" in sys.argv

template = "C:/Users/OscarIvanMarta/scripts/template2.cpp" if use_template2 else "C:/Users/OscarIvanMarta/scripts/template.cpp"
if not os.path.exists(template):
    print(f"❌ No se encontró la plantilla '{template}'.")
    sys.exit(1)

# Crear carpeta si no existe
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"📁 Carpeta '{folder_name}' creada.")
else:
    print(f"📁 Carpeta '{folder_name}' ya existe.")

# Generar archivos en la carpeta
LETTERS = string.ascii_uppercase
for i in range(n):
    filename = os.path.join(folder_name, f"{LETTERS[i]}.cpp")
    if os.path.exists(filename):
        print(f"⚠️  {filename} ya existe. Saltando...")
        continue
    shutil.copyfile(template, filename)
    print(f"✅ {filename} creado con plantilla '{template}'")

print("🚀 ¡Archivos generados correctamente!")

