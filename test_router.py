from router import classify_message

# Sample test messages
tests = [
    "Where is my order ORD1001?",
    "Do you have yoga mats?",
    "What's the weather today?"
]

for t in tests:
    result = classify_message(t)
    print(f"Message: {t}")
    print(f"Result: {result}")
    print("-" * 40)
