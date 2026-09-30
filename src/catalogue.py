import json

FILE_PATH = "data/products.json"

def load_catalogue():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def get_product(product_id):
    catalogue = load_catalogue()

    if product_id not in catalogue:
        raise ValueError(f"Product {product_id} not found")

    return catalogue[product_id]