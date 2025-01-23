import requests
import os



def chamignon_img_recup(output_folder, params, base_api_url, name):
    os.makedirs(output_folder, exist_ok=True)
    # Boucle sur les pages (1 à 5)
    for page in range(1, 2):
        print(f"Traitement de la page {page}...")
        params["page"] = page
        response = requests.get(base_api_url, params=params)
        data = response.json()

        # Parcourir les observations et télécharger les images
        for obs in data.get("results", []):
            if "photos" in obs:
                for photo in obs["photos"]:
                    image_url = photo["url"].replace("square", "original")  # Meilleure qualité
                    image_id = photo["id"]
                    filename = os.path.join(output_folder, f"{name}_{image_id}.jpg")

                    # Télécharger l'image
                    img_response = requests.get(image_url)
                    if img_response.status_code == 200:
                        with open(filename, "wb") as f:
                            f.write(img_response.content)
                        print(f"Image téléchargée : {filename}")

    print("Téléchargement terminé.")

# Créer un dossier pour stocker les images
output_folder = "Amanita_Images"

# Base URL de l'API iNaturalist
base_api_url = "https://api.inaturalist.org/v1/observations"

# Paramètres pour la requête API
params = {
    "taxon_name": "Amanita",
    "page": 1,
    "per_page": 100,  # Nombre d'observations par page
}
#chamignon_img_recup(output_folder, params, base_api_url, "amanita")

output_folder = "Crimini_Images"

# Base URL de l'API iNaturalist
base_api_url = "https://api.inaturalist.org/v1/observations"

# Paramètres pour la requête API
params = {
    "taxon_id": "61395",
    "page": 1,
    "per_page": 100,  # Nombre d'observations par page
}
#chamignon_img_recup(output_folder, params, base_api_url, "crimini")

output_folder = "Oyster_Images"

# Base URL de l'API iNaturalist
base_api_url = "https://api.inaturalist.org/v1/observations"

# Paramètres pour la requête API
params = {
    "taxon_id": "48496",
    "page": 1,
    "per_page": 100,  # Nombre d'observations par page
}
chamignon_img_recup(output_folder, params, base_api_url, "oyster")