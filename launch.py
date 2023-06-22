import subprocess
import threading
import time

# Fonction pour exécuter une commande dans une fenêtre xterm avec une taille personnalisée
def run_command_in_xterm(command, width, height):
    xterm_command = ['xterm', '-geometry', f"{width}x{height}", '-e', command]
    subprocess.Popen(xterm_command)

# Fonction pour exécuter le script spectre.py
def run_spectre_script():
    subprocess.call("python3 spectre.py", shell=True)

# Fonction pour exécuter le script analyse.py
def run_analyse_script():
    run_command_in_xterm("python3 analyse.py", 165, 60)

# Création des threads pour exécuter les scripts en parallèle
spectre_thread = threading.Thread(target=run_spectre_script)
analyse_thread = threading.Thread(target=run_analyse_script)

# Démarrage du thread spectre_thread
spectre_thread.start()

# Attendre 30 secondes
time.sleep(20)

# Démarrage du thread analyse_thread après 30 secondes
analyse_thread.start()

# Attendre la fin des threads
spectre_thread.join()
analyse_thread.join()
