import datetime
orders = []  
order_id_counter = 1

def record_order():
    global order_id_counter
    print("\n--- New Repair Order ---")
    customer = input("Enter customer name: ")
    device   = input("Enter device type: ")
    issue    = input("Enter device issue: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")

    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except:
        print(" Invalid date format. Please use DD-MM-YYYY.")
        return

    order = {
        "order_id": order_id_counter,
        "customer": customer,
        "device": device,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending",
        "parts": [],
        "repair_fee": 0,
    }
    orders.append(order)
    print(f"Order recorded successfully! Order ID: {order_id_counter}")
    order_id_counter += 1


def complete_repair():
    if not orders:
        print("\n No orders available.")
        return

    try:
        order_id = int(input("Enter Order ID to complete: "))
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    order = next((o for o in orders if o["order_id"] == order_id), None)

    if not order:
        print(" Order not found.")
        return

    if order["status"] == "Completed":
        print(" This order is already completed.")
        return

    print(f"\n--- Completing Order #{order_id} ---")
    parts_count = int(input("Enter number of parts replaced: "))

    for i in range(parts_count):
        part_name = input(f" Part {i+1} name: ")
        try:
            part_cost = float(input(f" Part {i+1} cost: "))
        except ValueError:
            print(" Invalid cost. Skipping this part.")
            continue
        order["parts"].append((part_name, part_cost))

    try:
        order["repair_fee"] = float(input("Enter repair service fee: "))
    except ValueError:
        print(" Invalid fee. Setting to 0.")
        order["repair_fee"] = 0

    order["status"] = "Completed"
    print(" Repair marked as completed.")


def generate_invoice():
    if not orders:
        print("\n No orders available.")
        return

    try:
        order_id = int(input("Enter Order ID for invoice: "))
    except ValueError:
        print(" Invalid input. Enter a number.")
        return

    order = next((o for o in orders if o["order_id"] == order_id), None)

    if not order:
        print(" Order not found.")
        return

    if order["status"] != "Completed":
        print(" Repair not completed yet. Invoice unavailable.")
        return

    print("\n====== FixTrack Invoice ======")
    print(f"Order ID   : {order['order_id']}")
    print(f"Customer   : {order['customer']}")
    print(f"Device     : {order['device']}")
    print(f"Issue      : {order['issue']}")
    print(f"Due Date   : {order['due_date']}")
    print("-------------------------------")

    subtotal = order["repair_fee"] + sum(cost for _, cost in order["parts"])
    tax = subtotal * 0.18 
    discount = 0

    apply_discount = input("Apply discount? (y/n): ").lower()
    if apply_discount == "y":
        try:
            discount = float(input("Enter discount amount: "))
        except ValueError:
            print("Invalid discount. Setting to 0.")
            discount = 0

    total = subtotal + tax - discount

    print(f"Repair Fee : ₹{order['repair_fee']:.2f}")
    for part, cost in order["parts"]:
        print(f"Part       : {part} - ₹{cost:.2f}")
    print(f"Subtotal   : ₹{subtotal:.2f}")
    print(f"Tax (18%)  : ₹{tax:.2f}")
    print(f"Discount   : ₹{discount:.2f}")
    print("-------------------------------")
    print(f"TOTAL      : ₹{total:.2f}")
    print("===============================")


def view_orders():
    if not orders:
        print("\n No orders found.")
        return

    print("\n--- All Repair Orders ---")
    for order in orders:
        print(
            f"ID: {order['order_id']} | Customer: {order['customer']} | "
            f"Device: {order['device']} | Status: {order['status']} | Due: {order['due_date']}"
        )


def main():
   
    while True:
        print("\n===== FixTrack Menu =====")
        print("1. Record New Repair Order")
        print("2. Complete Repair & Add Billing")
        print("3. Generate Invoice")
        print("4. View All Orders")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            record_order()
        elif choice == "2":
            complete_repair()
        elif choice == "3":
            generate_invoice()
        elif choice == "4":
            view_orders()
        elif choice == "5":
            print(" Exiting FixTrack.thanks for visite site!")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
