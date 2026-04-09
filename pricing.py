def calculate_total_price(items, tax_rate):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    tax = total * tax_rate
    return total + tax
