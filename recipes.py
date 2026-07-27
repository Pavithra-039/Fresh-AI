def get_recipes(items):
    recipe_db = {
        "banana": ["Banana Smoothie", "Banana Pancakes"],
        "egg": ["Omelette", "Egg Fried Rice"],
        "tomato": ["Tomato Soup", "Pasta Sauce"],
        "milk": ["Milkshake", "Custard"],
        "bread": ["Sandwich", "French Toast"]
    }

    suggestions = []
    for item in items:
        if item in recipe_db:
            suggestions.extend(recipe_db[item])

    return list(set(suggestions)) if suggestions else ["No recipes found"]