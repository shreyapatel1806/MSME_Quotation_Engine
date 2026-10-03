from src.quatation import create_quotation

def main():
    customer_name = input("Enter customer name: ")

    items = []

    while True:

        product_id = input(
            "Enter product ID (or 'done' to finish): "
        )

        if product_id == "done" or product_id == "DONE":
            break
        try:

            quantity = int(input("Enter quantity: "))

            items.append({
                "product_id": product_id,
                "quantity": quantity
            })

        
        except ValueError as error:
            print("Error:",error)


    if not items:
        print("No products added.")
        return
    try:
        quotation = create_quotation(items)

        print("\n=========== QUATATION ===========")
        print("Customer:",customer_name)

        for item in quotation["items"]:
            print(f'{item["name"]} | '
            f'{item["quantity"]} x '
            f'₹{item["unit_price"]} = '
            f'₹{item["total"]}'
        )

        print("---------------------------------")
        print("Subtotal:",quotation["subtotal"])
        print("Discount:",quotation["discount"])
        print("Tax:",quotation["tax"])
        print("Grand Total:",quotation["grand_total"])


    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()