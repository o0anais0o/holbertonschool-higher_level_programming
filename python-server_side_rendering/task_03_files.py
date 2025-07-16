from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Aide à la lecture du fichier JSON
def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        return []

# Aide à la lecture à partir d'un fichier CSV
def read_csv_file(file_path):
    try:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            return [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                for row in reader
            ]
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json_file("products.json")
    elif source == 'csv':
        products = read_csv_file("products.csv")
    else:
        error = "Wrong source. Please specify 'json' or 'csv'."
        return render_template("product_display.html", error=error)

    # Si un ID est fourni, filtrer les produits
    if product_id is not None:
        filtered = [p for p in products if p["id"] == product_id]
    if not filtered:
        error = f"Product not found"
        products = []  # Aucune donnée produit à afficher
    else:
        products = filtered

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
