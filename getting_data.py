import requests
import zipfile
from pathlib import Path

data_path = Path(r"/home/ash/FoodVision/data")
image_path = data_path / "pizza_steak_sushi"

#If the image doesnt exist, downloading it and preparing it
if image_path.is_dir():
    print(f"{image_path} directory already exists")
else:
    print(f"No {image_path} is present. Creating one......")
    image_path.mkdir(parents=True, exist_ok=True)


