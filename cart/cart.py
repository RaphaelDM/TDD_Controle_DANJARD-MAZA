import json
import os
from datetime import datetime
from dataclasses import dataclass

#Structure de données pour un produit
@dataclass
class Product:
    name: str
    price: float

class Cart:
    def __init__(self):
        self._items = []          
        self._discount_pct = 0.0

    # Méthode pour ajouter un produit au panier
    def add_product(self, name: str, price: float):
        if price < 0:
            raise InvalidPriceError("Negative price not allowed")
        self._items.append(Product(name=name, price=float(price)))

    # Méthode pour supprimer un produit du panier par nom
    def remove_product(self, name: str):
        # Version “première occurrence”
        for idx, prod in enumerate(self._items):
            if prod.name == name:
                del self._items[idx]
                break
    
    # Méthode pour appliquer une remise en pourcentage
    def apply_discount(self, percentage: float):
        self._discount_pct = float(percentage)

    # Méthode pour calculer le total du panier
    def get_total(self) -> float:
        total = sum(p.price for p in self._items)
        if self._discount_pct:
            total *= (1 - self._discount_pct / 100.0)
        return round(total, 2)

    # Méthode pour sauvegarder le panier dans un fichier JSON et créer une archive horodatée
    def save_to_file(self, filepath: str):
        data = {
            "items": [{"name": p.name, "price": p.price} for p in self._items],
            "discount": self._discount_pct,
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        base_dir = os.path.dirname(filepath) or "."
        archives_dir = os.path.join(base_dir, "archives")
        os.makedirs(archives_dir, exist_ok=True)

        ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        name, ext = os.path.splitext(os.path.basename(filepath))
        if not ext:
            ext = ".json"
        archive_path = os.path.join(archives_dir, f"{name}_{ts}{ext}")

        with open(archive_path, "w", encoding="utf-8") as af:
            json.dump(data, af, ensure_ascii=False)

    # Méthode pour charger le panier depuis un fichier JSON
    def load_from_file(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._items = [Product(it["name"], float(it["price"])) for it in data.get("items", [])]
        self._discount_pct = float(data.get("discount", 0.0))

    
# Exception personnalisée pour les prix invalides    
class InvalidPriceError(Exception):
    pass
    
