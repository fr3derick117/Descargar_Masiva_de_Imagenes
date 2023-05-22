import requests
import os

# API endpoint
url = "https://api.pexels.com/v1/search"

# Api Key
api_key = "oXyuVXd238y85nyxrE5kJKKTJsoqcRdtRMop4vAWchwA6PwCMCbH5Ahb"

# Escribe lo que quieres de imagen
query = "Tucan"

# Cuantas imagenes quieres?
num_images = 100

# Escribe el nombre de la carpate donde quieres que se guarde
dir_name = "cat_images"

# Api
headers = {
    "Authorization": api_key
}

params = {
    "query": query,
    "per_page": num_images
}


response = requests.get(url, headers=headers, params=params)

data = response.json()

if not os.path.exists(dir_name):
    os.makedirs(dir_name)


for i, photo in enumerate(data["photos"]):
    img_url = photo["src"]["large"]
    response = requests.get(img_url)

    with open(f"{dir_name}/cat{i+1}.jpg", "wb") as f:
        f.write(response.content)