import json
import os

DATA_DIR = "/opt/airflow/data/ventes"
RAW_FILE = f"{DATA_DIR}/ventes_brutes.json"
CLEAN_FILE = f"{DATA_DIR}/ventes_propres.json"
REPORT_FILE = f"{DATA_DIR}/rapport_ventes.txt"


def extraire_ventes():
    os.makedirs(DATA_DIR, exist_ok=True)

    donnees = [
        {"produit": "Clavier", "prix": "50", "quantite": "3"},
        {"produit": "Souris", "prix": "25", "quantite": "5"},
        {"produit": "Écran", "prix": "200", "quantite": "2"},
        {"produit": "Casque", "prix": "80", "quantite": "4"},
        {"produit": "Webcam", "prix": "60", "quantite": "3"},
    ]

    with open(RAW_FILE, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)

    print("Extraction des ventes terminée")


def valider_ventes():
    with open(RAW_FILE, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    colonnes = ["produit", "prix", "quantite"]

    for vente in donnees:
        for colonne in colonnes:
            if colonne not in vente:
                raise ValueError(f"Colonne manquante : {colonne}")

    print("Validation réussie")


def transformer_ventes():
    with open(RAW_FILE, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    ventes_propres = []

    for vente in donnees:
        prix = float(vente["prix"])
        quantite = int(vente["quantite"])

        ventes_propres.append({
            "produit": vente["produit"].upper(),
            "prix": prix,
            "quantite": quantite,
            "chiffre_affaires": prix * quantite
        })

    with open(CLEAN_FILE, "w", encoding="utf-8") as fichier:
        json.dump(ventes_propres, fichier, ensure_ascii=False, indent=4)

    print("Transformation terminée")


def generer_rapport():
    with open(CLEAN_FILE, "r", encoding="utf-8") as fichier:
        ventes = json.load(fichier)

    ca_total = sum(v["chiffre_affaires"] for v in ventes)
    meilleur_produit = max(ventes, key=lambda v: v["chiffre_affaires"])

    lignes = [
        "RAPPORT DES VENTES",
        "==================",
        f"Nombre de produits : {len(ventes)}",
        f"Chiffre d'affaires total : {ca_total} €",
        f"Meilleure vente : {meilleur_produit['produit']} ({meilleur_produit['chiffre_affaires']} €)",
        "",
        "Détail des ventes :"
    ]

    for vente in ventes:
        lignes.append(
            f"- {vente['produit']} : {vente['quantite']} unités - "
            f"{vente['chiffre_affaires']} €"
        )

    rapport = "\n".join(lignes)

    with open(REPORT_FILE, "w", encoding="utf-8") as fichier:
        fichier.write(rapport)

    print(rapport)
