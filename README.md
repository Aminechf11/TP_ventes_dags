# TP Airflow - Pipeline ETL des ventes

## Description

Ce projet présente un pipeline ETL simple réalisé avec Apache Airflow.

L'objectif est de simuler le traitement de données de ventes à travers quatre étapes :

1. Extraction des données
2. Validation des données
3. Transformation des données
4. Génération d'un rapport

---

## Structure du DAG

```text
extract
   ↓
validate
   ↓
transform
   ↓
report
```

---

## Description des tâches

### Extract

Création d'un fichier JSON contenant des ventes fictives.

Exemple :

```json
{
    "produit": "Clavier",
    "prix": "50",
    "quantite": "3"
}
```

### Validate

Vérification que chaque vente contient les champs obligatoires :

- produit
- prix
- quantite

### Transform

Transformation des données :

- conversion des prix en nombre
- conversion des quantités en entier
- calcul du chiffre d'affaires

Exemple :

```json
{
    "produit": "CLAVIER",
    "prix": 50.0,
    "quantite": 3,
    "chiffre_affaires": 150.0
}
```

### Report

Génération d'un rapport contenant :

- le nombre de produits
- le chiffre d'affaires total
- le produit ayant généré le plus de revenus

Exemple :

```text
RAPPORT DES VENTES
==================
Nombre de produits : 5
Chiffre d'affaires total : 1175.0 €
Meilleure vente : ÉCRAN (400.0 €)
```

---

## Technologies utilisées

- Python 3
- Apache Airflow
- JSON

---

## Fichiers du projet

```text
.
├── dags/
│   └── sales_dag.py
│   └──sales_pipeline.py
└── README.md
```

---

## Résultats

Le DAG s'exécute correctement dans Airflow et produit :

- un fichier de données brutes
- un fichier de données transformées
- un rapport récapitulatif des ventes

Chaque étape du pipeline est visible dans les logs Airflow et illustrée par les captures d'écran fournies dans le dossier `screenshots`.

---

## Auteur

Projet réalisé dans le cadre du TP Apache Airflow.
