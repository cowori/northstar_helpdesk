from flask import Flask, jsonify, request, send_from_directory
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from router import classify_message

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT_DIR, "data")

app = Flask(__name__, static_folder=ROOT_DIR, static_url_path="")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

@app.route("/")
def serve_index():
    return send_from_directory(ROOT_DIR, "index.html")

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

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    result = classify_message(user_message)
    intent = result["intent"]
    value = result["value"]

    if intent == "order_status":
        orders = load_json("orders.json")
        order = orders.get(value.upper()) if value else None
        if order:
            reply = f"Your order {order['order_id']} is currently: {order['status']} (ETA: {order['eta']})"
        else:
            reply = "I couldn't find that order. Can you double-check the order ID?"

    elif intent == "stock_check":
        inventory = load_json("inventory.json")
        item = inventory.get(value.lower()) if value else None
        if item:
            if "in_stock" in item:
                in_stock = item["in_stock"]
            elif "quantity" in item:
                in_stock = item["quantity"] > 0
            else:
                in_stock = True
            reply = f"Yes, {value} is in stock." if in_stock else f"Sorry, {value} is currently out of stock."
        else:
            reply = "I couldn't find that item. Can you tell me the exact product name?"

    else:
        reply = "I'm not sure I understood - try asking about an order status or item stock."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
