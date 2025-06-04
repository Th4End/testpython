from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from tqdm import tqdm

# Connexion à la base de données
DATABASE_URL = "mysql+mysqlconnector://test:roottest@172.31.145.178:3306/javatest"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Définition de la classe Product
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)

# ETL : Extraction / Transformation / Chargement
def etl_load_products():
    Base.metadata.drop_all(engine)    # Supprime la table si elle existe
    Base.metadata.create_all(engine)  # Crée la table

    # Données simulées (étape Extract & Transform)
    products_data = [
        {"name": "Laptop", "price": 1200.0},
        {"name": "Smartphone", "price": 800.0},
        {"name": "Tablet", "price": 450.0}
    ]

    print("Chargement des produits en cours...")
    for item in tqdm(products_data, desc="Insertion", unit="produit"):
        product = Product(name=item["name"], price=item["price"])
        session.add(product)

    session.commit()
    print("✔️ Produits chargés avec succès.")

if __name__ == "__main__":
    etl_load_products()
