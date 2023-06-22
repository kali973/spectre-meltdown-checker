import json
from tinydb import TinyDB

# Réinitialisation de la base de données "resultat"
db = TinyDB('resultat')
db.truncate()

# Lecture du fichier output_db.json
with open('output_db.json', 'r') as file:
    data = json.load(file)

# Parcours des lignes du fichier et insertion dans la base de données
previous_cve_line = None
for line in data["_default"]["1"]["output"].split('\n'):
    if "CVE-2017-57" in line:
        previous_cve_line = line
        continue

    if "YES" in line:
        if previous_cve_line is not None:
            db.insert({'cve_line': previous_cve_line, 'yes_line': line})
        else:
            db.insert({'yes_line': line})

# Lecture du contenu de la base de données
results = db.all()

# Affichage des lignes contenant "CVE" avant chaque ligne contenant "YES"
print("Résultats de la recherche dans la base de données 'resultat':")
for result in results:
    if 'cve_line' in result:
        print(result['cve_line'])
    print(result['yes_line'])

# Pause à la fin pour empêcher la fermeture immédiate de la fenêtre
input("Appuyez sur Entrée pour quitter...")
