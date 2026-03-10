import json
import os

def load_crops():

    path = os.path.join("data", "crops.json")

    with open(path, "r", encoding="utf-8") as f:
        crops = json.load(f)

    return crops


def get_crop_info(crop_name):

    crops = load_crops()

    crop_name = crop_name.strip().title()

    return crops.get(crop_name)
