from cart.cart import Cart

# test pour ajouter des produits et vérifier le total
def test_add_products_and_total():
    # Arrange
    cart = Cart()
    # Act
    cart.add_product("Café", 3.5)
    cart.add_product("Croissant", 2.0)
    # Assert
    assert cart.get_total() == 5.5
    
    

