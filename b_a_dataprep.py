import os
from a_getting_data import image_path
dir_path = ("/home/ash/FoodVision/data/pizza_steak_sushi")

def walk_through_dir(dir_path):
    """walks through dir_path returning its contents"""

    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(f"There are {len(dirnames)} directories and {len(filenames)} images in {dirpath}")

train_dir = image_path / "train"
test_dir = image_path / "test"

print(train_dir, test_dir)