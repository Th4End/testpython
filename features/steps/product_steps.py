import requests
from behave import when, then

BASE_URL = "http://localhost:8000/api/products"

@when('je consulte la liste des produits')
def step_consulter_liste(context):
    context.response = requests.get(BASE_URL)

@then('je reçois une réponse avec 2 produits')
def step_verifier_liste(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) == 2

@when('je consulte le produit avec l\'identifiant {id:d}')
def step_consulter_produit_par_id(context, id):
    context.response = requests.get(f"{BASE_URL}/{id}")

@then('je reçois le produit nommé "{nom}"')
def step_verifier_nom_produit(context, nom):
    assert context.response.status_code == 200
    assert context.response.json()["name"] == nom

@then('je reçois une erreur 404')
def step_erreur_404(context):
    assert context.response.status_code == 404
