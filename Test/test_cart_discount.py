from cart.cart import Cart

# test pour appliquer une remise sur le total du panier
def test_apply_discount_on_total():
    cart = Cart()
    cart.add_product("Livre", 20)
    cart.apply_discount(10)  # -10%
    assert cart.get_total() == 18

# test pour vérifier que la remise s'applique aux futurs articles ajoutés
def test_discount_applies_to_future_items():
    cart = Cart()
    cart.apply_discount(50) 
    cart.add_product("A", 10)
    cart.add_product("B", 10)
    assert cart.get_total() == 10 

# test pour vérifier que plusieurs remises successives écrasent la précédente
def test_multiple_discounts_overwrite_previous():
    cart = Cart()
    cart.add_product("A", 100)
    cart.apply_discount(10)
    cart.apply_discount(20)
    assert cart.get_total() == 80
