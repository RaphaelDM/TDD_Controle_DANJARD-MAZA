from cart.cart import Cart

# test pour supprimer un produit existant du panier
def test_remove_existing_product():
    # Arrange
    cart = Cart()
    
    # Act
    cart.add_product("Café", 3.5)
    cart.add_product("Croissant", 2.0)
    cart.remove_product("Café")
    
    # Assert
    assert cart.get_total() == 2.0

# test pour tenter de supprimer un produit qui n'existe pas dans le panier
def test_remove_nonexistent_product_is_noop():
    
    # Arrange
    cart = Cart()
    
    # Act
    cart.add_product("Café", 3.5)
    cart.remove_product("Thé")
    # Assert
    assert cart.get_total() == 3.5