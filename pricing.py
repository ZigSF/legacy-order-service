def calculate_total_price(items, tax_rate):
    if not isinstance(items, list):
        raise TypeError("items must be a list of dictionaries")

    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        raise TypeError("tax_rate must be a number")

    if tax_rate < 0:
        raise ValueError("tax_rate must be non-negative")

    total = 0

    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise TypeError(
                f"items[{index}] must be a dictionary with 'price' and 'quantity' keys"
            )

        if "price" not in item or "quantity" not in item:
            raise ValueError(
                f"items[{index}] must contain both 'price' and 'quantity' keys"
            )

        price = item["price"]
        quantity = item["quantity"]

        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError(f"items[{index}]['price'] must be a number")

        if not isinstance(quantity, (int, float)) or isinstance(quantity, bool):
            raise TypeError(f"items[{index}]['quantity'] must be a number")

        if price < 0:
            raise ValueError(f"items[{index}]['price'] must be non-negative")

        if quantity < 0:
            raise ValueError(f"items[{index}]['quantity'] must be non-negative")

        total += price * quantity

    tax = total * tax_rate
    return total + tax
