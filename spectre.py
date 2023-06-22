#!/usr/bin/env python3
import subprocess
import os
import glob

# Supprime les fichiers commençant par "resultat"
for file in glob.glob("resultat*"):
    os.remove(file)

# Vérifie si xterm est installé
if subprocess.call("command -v xterm &> /dev/null", shell=True) != 0:
    print("xterm n'est pas installé. Installation en cours...")
    subprocess.call("sudo apt-get update", shell=True)
    subprocess.call("sudo apt-get install xterm -y", shell=True)

# Vérifie si TinyDB est installé
if (
        subprocess.call("command -v python3 &> /dev/null", shell=True) != 0
        or subprocess.call("python3 -c 'import tinydb' &> /dev/null", shell=True) != 0
):
    print("TinyDB n'est pas installé. Installation en cours...")
    subprocess.call("sudo apt-get update", shell=True)
    subprocess.call("sudo apt-get install python3-pip -y", shell=True)
    subprocess.call("sudo pip3 install tinydb", shell=True)

# Donne les permissions d'exécution au fichier spectre-meltdown-checker.sh
subprocess.call("chmod +x spectre-meltdown-checker.sh", shell=True)

# Nom du fichier de sortie pour enregistrer le contenu de l'affichage
output_file = "spectre_output.txt"

# Obtenir les dimensions de l'écran
screen_width = int(
    subprocess.check_output("xwininfo -root | awk '/Width/ {print $2}'", shell=True)
)
screen_height = int(
    subprocess.check_output("xwininfo -root | awk '/Height/ {print $2}'", shell=True)
)

# Calculer les coordonnées de la fenêtre xterm pour la centrer
xterm_width = 180
xterm_height = 40
xterm_x = (screen_width - xterm_width) // 2
xterm_y = (screen_height - xterm_height) // 2

# Exécute le script spectre-meltdown-checker.sh avec l'option --explain en utilisant sudo et enregistre toute la sortie dans le fichier de sortie
subprocess.call(
    f"xterm -hold -geometry {xterm_width}x{xterm_height}+{xterm_x}+{xterm_y} -e './spectre-meltdown-checker.sh --explain' > {output_file}",
    shell=True,
)

# Importe TinyDB dans un script Python pour enregistrer le contenu du fichier dans la base de données
import tinydb

# Chemin vers le fichier de sortie
output_file = "spectre_output.txt"

# Initialise la base de données TinyDB
db = tinydb.TinyDB("output_db.json")

# Lit le contenu du fichier de sortie
with open(output_file, "r") as file:
    content = file.read()

# Enregistre le contenu dans la base de données
db.insert({"output": content})

# Supprime le fichier de sortie
os.remove(output_file)

# Termine le script
exit(0)
