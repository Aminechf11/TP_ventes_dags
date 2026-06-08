import json, os, tempfile

tmp = tempfile.mkdtemp()
RAW_FILE = os.path.join(tmp, "ventes_brutes.json")
CLEAN_FILE = os.path.join(tmp, "ventes_propres.json")
REPORT_FILE = os.path.join(tmp, "rapport_ventes.txt")

# extraire_ventes
donnees = [
    {"produit": "Clavier", "prix": "50", "quantite": "3"},
    {"produit": "Souris", "prix": "25", "quantite": "5"},
    {"produit": "Ecran", "prix": "200", "quantite": "2"},
    {"produit": "Casque", "prix": "80", "quantite": "4"},
    {"produit": "Webcam", "prix": "60", "quantite": "3"},
]
with open(RAW_FILE, "w", encoding="utf-8") as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)
print("Extraction des ventes terminee")

# valider_ventes
with open(RAW_FILE, "r", encoding="utf-8") as f:
    donnees = json.load(f)
for vente in donnees:
    for col in ["produit", "prix", "quantite"]:
        if col not in vente:
            raise ValueError(f"Colonne manquante : {col}")
print("Validation reussie")

# transformer_ventes
with open(RAW_FILE, "r", encoding="utf-8") as f:
    donnees = json.load(f)
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
with open(CLEAN_FILE, "w", encoding="utf-8") as f:
    json.dump(ventes_propres, f, ensure_ascii=False, indent=4)
print("Transformation terminee")

# generer_rapport
with open(CLEAN_FILE, "r", encoding="utf-8") as f:
    ventes = json.load(f)
ca_total = sum(v["chiffre_affaires"] for v in ventes)
meilleur = max(ventes, key=lambda v: v["chiffre_affaires"])
rapport = (
    "\nRAPPORT DES VENTES\n"
    "==================\n"
    f"Nombre de produits : {len(ventes)}\n"
    f"Chiffre d'affaires total : {ca_total} EUR\n"
    f"Meilleure vente : {meilleur['produit']} ({meilleur['chiffre_affaires']} EUR)\n"
)
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write(rapport)
print(rapport)
print(f"Fichiers generes dans : {tmp}")
