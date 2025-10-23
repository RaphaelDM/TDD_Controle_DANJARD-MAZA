import io
import builtins
import os
from datetime import datetime
from cart.cart import Cart
import types
import pytest

# Faux système de fichiers en mémoire
class FakeFS:
    """Filesystem fake en mémoire pour mocker open() et makedirs()."""
    def __init__(self):
        self.files = {}   # path -> contenu
        self.dirs = set() # dossiers "créés"

    def open(self, path, mode="r", *args, **kwargs):
        p = str(path)
        if "w" in mode:
            buf = io.StringIO()
            def _close_and_persist(b=buf, path=p, self=self):
                self.files[path] = b.getvalue()
                b.close_orig()
            buf.close_orig = buf.close
            buf.close = _close_and_persist
            return buf
        elif "r" in mode:
            if p not in self.files:
                raise FileNotFoundError(p)
            return io.StringIO(self.files[p])
        else:
            raise ValueError(f"Unsupported mode {mode}")

    def makedirs(self, path, exist_ok=False):
        self.dirs.add(str(path))

def test_archives_created_with_timestamps(monkeypatch):
    #arrange
    fs = FakeFS()
    monkeypatch.setattr(builtins, "open", fs.open, raising=True)
    monkeypatch.setattr(os, "makedirs", fs.makedirs, raising=True)

    # Deux classes factices pour simuler datetime.now() avec des timestamps différents
    class FakeDT1:
        @staticmethod
        def now():
            return datetime(2025, 1, 1, 12, 0, 0)

    class FakeDT2:
        @staticmethod
        def now():
            return datetime(2025, 1, 1, 12, 0, 5) 
    cart = Cart()
    
    
    #act
    cart.add_product("Livre", 10)

    # 1er save() avec FakeDT1
    monkeypatch.setattr("cart.cart.datetime", FakeDT1, raising=True)
    cart.save_to_file("panier.json")

    # 2e save() avec FakeDT2
    monkeypatch.setattr("cart.cart.datetime", FakeDT2, raising=True)
    cart.save_to_file("panier.json")

    #assert
    # le dossier archives doit avoir été "créé"
    assert any("archives" in d for d in fs.dirs)

    # on récupère tous les fichiers écrits sous archives/
    archive_files = [p for p in fs.files.keys() if "/archives/" in p or "\\archives\\" in p]
    assert len(archive_files) == 2, f"attendu 2 archives, obtenu: {archive_files}"

    # les noms doivent contenir la date
    assert "2025-01-01" in archive_files[0]
    assert "2025-01-01" in archive_files[1]
    assert archive_files[0] != archive_files[1]
