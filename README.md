# 🛒 Shopping Cart (TDD)

[![tests](https://github.com/RaphaelDM/TDD_Controle_DANJARD-MAZA/actions/workflows/tests.yml/badge.svg)](https://github.com/RaphaelDM/TDD_Controle_DANJARD-MAZA/actions/workflows/tests.yml)

Un module simple de gestion de panier e-commerce, développé en TDD
(Test Driven Development : RED → GREEN → REFACTOR).

## Fonctionnalités principales

- Ajout et suppression de produits (nom + prix)
- Application d’une remise en pourcentage
- Gestion d’erreurs (prix négatif → `InvalidPriceError`)
- Sauvegarde et chargement du panier au format JSON
- Historique des sauvegardes horodatées dans `/archives`
- Tests unitaires complets avec `pytest`
- Mock du système de fichiers (aucun accès disque réel)
- Refactor propre avec `@dataclass` `Product`

## Installation

Installer les dépendances :

```bash
pip install pytest coverage
```

## Exécution des tests

Lancer tous les tests :

```bash
python -m pytest -q
```
Pour plus detaile

```bash
python -m pytest -v 
```

Tous les tests doivent passer.

## Rapport de couverture

Générer le rapport de couverture :

```bash
python -m coverage run -m pytest -q 
python -m coverage html
```

Ouvrir le rapport HTML :

```
htmlcov/index.html
```
