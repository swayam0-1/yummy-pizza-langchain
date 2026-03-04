def calculate_bill(order_items: list) -> dict:
    """
    order_items: list of dicts like
    [{"name": "Margherita", "size": "Medium", "qty": 1, "price": 249}, ...]
    """
    subtotal = sum(item["price"] * item.get("qty", 1) for item in order_items)
    tax = round(subtotal * 0.05, 2)  # 5% GST
    total = round(subtotal + tax, 2)

    return {
        "items": order_items,
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

def format_bill(bill: dict) -> str:
    text = "\n🧾 *YOUR ORDER BILL*\n"
    text += "=" * 30 + "\n"
    for item in bill["items"]:
        qty = item.get("qty", 1)
        name = item["name"]
        size = item.get("size", "")
        price = item["price"] * qty
        size_str = f"({size})" if size else ""
        text += f"  {name} {size_str} x{qty}  →  ₹{price}\n"
    text += "-" * 30 + "\n"
    text += f"  Subtotal     :  ₹{bill['subtotal']}\n"
    text += f"  GST (5%)     :  ₹{bill['tax']}\n"
    text += f"  *TOTAL       :  ₹{bill['total']}*\n"
    text += "=" * 30 + "\n"
    return text
