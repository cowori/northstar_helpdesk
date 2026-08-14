from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

@app.route("/api/order-status/<order_id>")
def order_status(order_id):
    orders = load_json("orders.json")
    order = orders.get(order_id.upper())
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order)

@app.route("/api/stock-check/<item_name>")
def stock_check(item_name):
    inventory = load_json("inventory.json")
    item = inventory.get(item_name.lower())
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
