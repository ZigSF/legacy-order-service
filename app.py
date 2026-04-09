from pricing import calculate_total_price
from utils import load_sample_orders

def main():
    orders = load_sample_orders()

    results = []

    for order in orders:
        total = calculate_total_price(order["items"], order["tax_rate"])
        results.append({
            "order_id": order["id"],
            "total": total
        })

    print("Order Results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
