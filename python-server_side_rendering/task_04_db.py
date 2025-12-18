#!/usr/bin/python3
"""Flask application to display products from JSON, CSV, or SQLite."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file(filepath):
    """Read and parse data from a JSON file."""
    with open(filepath, 'r') as file:
        return json.load(file)


def read_csv_file(filepath):
    """Read and parse data from a CSV file."""
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sqlite_db(db_path):
    """Read and parse data from a SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite based on query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Read data from the appropriate source
    try:
        if source == 'json':
            products_list = read_json_file('products.json')
        elif source == 'csv':
            products_list = read_csv_file('products.csv')
        else:
            products_list = read_sqlite_db('products.db')
    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    except sqlite3.Error:
        return render_template('product_display.html', error="Database error")

    # Filter by id if provided
    if product_id is not None:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
