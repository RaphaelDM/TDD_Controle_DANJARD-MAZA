import io
import builtins
from cart.cart import Cart

# Une fausse implémentation du système de fichiers en mémoire
class FakeFileSystem:
    def __init__(self):
        self.files = {}

    def open(self, path, mode='r', *args, **kwargs):
        if 'w' in mode:
            buf = io.StringIO()
            def save_on_close(b=buf, p=path, fs=self):
                fs.files[p] = b.getvalue()
                b.close_orig()
            buf.close_orig = buf.close
            buf.close = save_on_close
            return buf
        elif 'r' in mode:
            if path not in self.files:
                raise FileNotFoundError(path)
            return io.StringIO(self.files[path])
        else:
            raise ValueError(f"Unsupported mode {mode}")


def test_save_and_load(monkeypatch):
    
    #arrange
    fs = FakeFileSystem()
    monkeypatch.setattr(builtins, "open", fs.open)
    
    #act
    cart = Cart()
    cart.add_product("Livre", 10)
    cart.add_product("Stylo", 2.5)
    cart.save_to_file("panier.json")
    new_cart = Cart()
    new_cart.load_from_file("panier.json")

    #assert
    assert new_cart.get_total() == 12.5
