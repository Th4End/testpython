Feature: Récupération des produits

  Scenario: Obtenir la liste des produits
    When je consulte la liste des produits
    Then je reçois une réponse avec 2 produits

  Scenario: Obtenir un produit existant
    When je consulte le produit avec l'identifiant 1
    Then je reçois le produit nommé "Laptop"

  Scenario: Obtenir un produit inexistant
    When je consulte le produit avec l'identifiant 999
    Then je reçois une erreur 404
