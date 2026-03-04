MENU = {
    "pizzas": [
        {"id": 1, "name": "Margherita", "emoji": "🍕", "description": "Classic tomato & cheese", "prices": {"Small": 149, "Medium": 249, "Large": 349}},
        {"id": 2, "name": "Pepperoni", "emoji": "🍖", "description": "Loaded with pepperoni", "prices": {"Small": 179, "Medium": 279, "Large": 399}},
        {"id": 3, "name": "Veggie Delight", "emoji": "🥦", "description": "Bell peppers, olives, mushrooms", "prices": {"Small": 159, "Medium": 259, "Large": 359}},
        {"id": 4, "name": "BBQ Chicken", "emoji": "🍗", "description": "Smoky BBQ with chicken chunks", "prices": {"Small": 199, "Medium": 299, "Large": 429}},
        {"id": 5, "name": "Paneer Tikka", "emoji": "🧀", "description": "Spicy Indian paneer pizza", "prices": {"Small": 169, "Medium": 269, "Large": 379}},
    ],
    "sides": [
        {"id": 6, "name": "Garlic Bread", "emoji": "🥖", "price": 79},
        {"id": 7, "name": "Coleslaw", "emoji": "🥗", "price": 59},
        {"id": 8, "name": "Potato Wedges", "emoji": "🍟", "price": 99},
    ],
    "drinks": [
        {"id": 9, "name": "Coca Cola", "emoji": "🥤", "price": 49},
        {"id": 10, "name": "Sprite", "emoji": "🥤", "price": 49},
        {"id": 11, "name": "Water Bottle", "emoji": "💧", "price": 29},
    ]
}

def get_menu_text():
    text = "🍕 *PIZZA BOT MENU* 🍕\n"
    text += "=" * 30 + "\n\n"

    text += "🍕 *PIZZAS*\n"
    for p in MENU["pizzas"]:
        text += f"{p['emoji']} {p['name']} - {p['description']}\n"
        text += f"   S: ₹{p['prices']['Small']} | M: ₹{p['prices']['Medium']} | L: ₹{p['prices']['Large']}\n"

    text += "\n🍽️ *SIDES*\n"
    for s in MENU["sides"]:
        text += f"{s['emoji']} {s['name']} - ₹{s['price']}\n"

    text += "\n🥤 *DRINKS*\n"
    for d in MENU["drinks"]:
        text += f"{d['emoji']} {d['name']} - ₹{d['price']}\n"

    text += "\n" + "=" * 30
    return text
