from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        return []

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

def read_sqlite_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # pour récupérer un dict-like
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convertir les rows en liste de dicts
        products = []
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        return products
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
    elif source == 'sql':
        products = read_sqlite_db("products.db")
    else:
        error = "Wrong source. Please specify 'json', 'csv' or 'sql'."
        return render_template("product_display.html", error=error)

    if product_id is not None:
        filtered = [p for p in products if p["id"] == product_id]
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template("product_display.html", products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True)
