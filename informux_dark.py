import pyfiglet
import os
import time
import sys
# Leer el archivo
with open("INFORMUX_DARK.txt", "r") as f:
    logo = f.read()

# Obtener el ancho de la consola
console_width = os.get_terminal_size().columns

# Centrar el logo sin agregar espacios adicionales
for line in logo.splitlines():
    line_length = len(line)
    spaces = (console_width - line_length) // 2
    print(' ' * spaces + line)

opcion1 = pyfiglet.figlet_format("metasploit . . . 1")
opcion2 = pyfiglet.figlet_format("i-haklab . . . 2")
opcion3 = pyfiglet.figlet_format("DESKTOP . . . 3")
opcion4 = pyfiglet.figlet_format("EXIT . . . 4")
print(opcion1,opcion2,opcion3,opcion4)

usuario = input("elige una opcion: ")
if usuario == '1':
           os.system('cls' if os.name == 'nt' else 'clear')
           metasploit = pyfiglet.figlet_format("INSTALANDO METASPLOIT")
           print(metasploit)
           os.system('yes|apt install wget gnupg && \
mkdir -p $PREFIX/etc/apt/sources.list.d && \
wget https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -O \
$PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list && \
curl -fsSL "https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/dists/stable/public_key.gpg" \
|gpg --dearmor|tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null && \
apt update && apt install metasploit-framework')
elif usuario == '2':
             os.system('cls' if os.name == 'nt' else 'clear')             
             ihaklab = pyfiglet.figlet_format("INSTALANDO I-HAKLAB")
             print(ihaklab)
             os.system('yes|apt install wget gnupg && \
mkdir -p $PREFIX/etc/apt/sources.list.d && \
wget https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -O \
$PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list && \
curl -fsSL "https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/dists/stable/public_key.gpg" \
|gpg --dearmor|tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null && \
apt update && apt install i-haklab')
elif usuario == '3':
             os.system('cls' if os.name == 'nt' else 'clear')
             repositorios = pyfiglet.figlet_format("INSTALANDO REPOCITORIOS")
             print(repositorios)
             os.system('yes|apt install wget gnupg && \
mkdir -p $PREFIX/etc/apt/sources.list.d && \
wget https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -O \
$PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list && \
curl -fsSL "https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/dists/stable/public_key.gpg" \
|gpg --dearmor|tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null && \
apt update')
             xfce4 = pyfiglet.figlet_format("INSTALANDO INTERFAS GRAFICA")
             print(xfce4)
             os.system('bash scripts/script1.sh')
             cmd = pyfiglet.figlet_format('creando comando')
             os.system('bash scripts/script2.sh')
             print("\033[91mEjecuta 'desktop-dark'\033[0m")
elif usuario == '4':
             sys.exit()
else:
    negacion = pyfiglet.figlet_format("opcion incorrecta")
    print(negacion)
    time.sleep(3)
    os.system('python informuX_dark.py')
