def print_receipt(products, vat_rate=0.23):
    total_price = 0
    print("---PARAGON---")

    for product in products:
        price_with_tax = product['cena_netto'] * (1 + vat_rate)
        total_price += price_with_tax
        print(f"{product['nazwa']}... {price_with_tax:.2f}")

    print(f"SUMA: {total_price:.2f}")

products = [
    {'nazwa': 'Mleko', 'cena_netto': 3.50},
    {'nazwa': 'Czekolada', 'cena_netto': 5.20}
]

print_receipt(products)