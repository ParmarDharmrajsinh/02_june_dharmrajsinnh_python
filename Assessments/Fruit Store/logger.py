# logger.py

def log_transaction(action, user, fruit, qty, price):
    """Log all transactions to a text file."""
    with open("transaction_log.txt", "a") as log:
        log.write(f"{action.title()} | User: {user} | Fruit: {fruit.title()} | Qty: {qty} | Price: ₹{price}\n")
