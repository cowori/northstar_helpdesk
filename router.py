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
        filler = ["do", "you", "have", "any", "is", "there", "a", "an", "the",
                   "in", "stock", "available", "of", "?", "got"]
        words = re.findall(r"[a-z]+", msg)
        item_words = [w for w in words if w not in filler]
        value = " ".join(item_words) if item_words else None
        return {"intent": "stock_check", "value": value}
    # Fallback
    return {"intent": "unrecognized", "value": None}
