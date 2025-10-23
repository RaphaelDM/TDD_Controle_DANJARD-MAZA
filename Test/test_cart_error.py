import pytest
from cart.cart import Cart, InvalidPriceError

# test pour ajouter un produit avec un prix négatif
def test_add_negative_price_raises():
    #arrange
    cart = Cart()
    # on vérifie qu'une exception est bien levée
    
    #act & assert
    with pytest.raises(InvalidPriceError):
        cart.add_product("Erreur", -5)
