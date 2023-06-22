#!/bin/bash

# Étape 1: Mettre à jour le système
echo "Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

# Étape 2: Installer les dépendances pour Docker
echo "Installation des dépendances pour Docker..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Étape 3: Ajouter la clé GPG de Docker
echo "Ajout de la clé GPG de Docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Étape 4: Ajouter le référentiel Docker aux sources APT
echo "Ajout du référentiel Docker aux sources APT..."
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Étape 5: Mettre à jour la liste des packages
echo "Mise à jour de la liste des packages..."
sudo apt update

# Étape 6: Installer Docker
echo "Installation de Docker..."
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Étape 7: Vérifier l'installation de Docker
echo "Vérification de l'installation de Docker..."
docker --version

# Étape 8: Installer Docker Compose
echo "Installation de Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Étape 9: Vérifier l'installation de Docker Compose
echo "Vérification de l'installation de Docker Compose..."
docker-compose --version

# Étape supplémentaire 1: Télécharger spectre-meltdown-checker.sh avec curl
echo "Téléchargement de spectre-meltdown-checker.sh avec curl..."
curl -L https://meltdown.ovh -o spectre-meltdown-checker.sh

# Étape supplémentaire 2: Télécharger spectre-meltdown-checker.sh avec wget
echo "Téléchargement de spectre-meltdown-checker.sh avec wget..."
wget https://meltdown.ovh -O spectre-meltdown-checker.sh

# Étape supplémentaire 3: Donner les permissions d'exécution à spectre-meltdown-checker.sh
echo "Donner les permissions d'exécution à spectre-meltdown-checker.sh..."
chmod +x spectre-meltdown-checker.sh

# Étape supplémentaire 4: Exécuter spectre-meltdown-checker.sh en tant que superutilisateur
echo "Exécution de spectre-meltdown-checker.sh en tant que superutilisateur..."
sudo ./spectre-meltdown-checker.sh

echo "Installation terminée avec succès !"
