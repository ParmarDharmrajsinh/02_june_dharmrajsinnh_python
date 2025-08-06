# logger.py

def log_transaction(action, user, fruit, qty, price):
    """Log all transactions to a text file using UTF-8 encoding."""
    with open("transaction_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{action.title()} | User: {user} | Fruit: {fruit.title()} | Qty: {qty} | Price: ₹{price}\n")
