import requests

def get_recipes(ingredients):
    api_key = "b3e7af2be55f47d29db10124e2dfcd68"
    ingredients_str = ",".join(ingredients)  # Join ingredients list
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients_str}&apiKey={api_key}"
    
    response = requests.get(url)
    recipes_list = []

    if response.status_code == 200:
        recipes = response.json()
        if recipes:
            for i, recipe in enumerate(recipes):
                title = recipe.get("title", "Unknown")
                image = recipe.get("image", "")
                recipes_list.append({"title": title, "image": image})
        else:
            print("No recipes found for the given ingredients.")
    else:
        print(f"Failed to fetch recipes. Status code: {response.status_code}")
        print("Response message:", response.text)
    return recipes_list