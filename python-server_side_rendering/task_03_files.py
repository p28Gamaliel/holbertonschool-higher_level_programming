#!/usr/bin/python3
"""Flask application to display products from JSON or CSV files."""
from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """Display products from JSON or CSV based on query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Read data from the appropriate file
    try:
        if source == 'json':
            products_list = read_json_file('products.json')
        else:
            products_list = read_csv_file('products.csv')
    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")

    # Filter by id if provided
    if product_id is not None:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
