import re

def classify_message(message: str) -> dict:
    msg = message.lower()

    # Order status intent
    if "order" in msg or "ord" in msg:
        match = re.search(r"(ord\d+)", msg)
        if match:
            return {"intent": "order_status", "value": match.group(1)}
        return {"intent": "order_status", "value": None}

    # Stock check intent
    if "stock" in msg or "have" in msg or "available" in msg:
        words = msg.split()
        return {"intent": "stock_check", "value": words[-1]}

    # Fallback
    return {"intent": "unrecognized", "value": None}
