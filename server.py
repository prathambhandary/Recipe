from flask import Flask, render_template, request, redirect, url_for
import recipe

app = Flask(__name__)

# Initialize the ingredients list
ingredients = []

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredient = request.form.get('ingredient')  # Corrected the typo 'ingridient' to 'ingredient'
        
        if ingredient:
            ingredients.append(ingredient)  # Add the ingredient to the list

        return redirect(url_for('home'))  # Redirect back to the home route to update the list
    
    return render_template("index.html", ingredients=ingredients)

@app.route("/result")
def result():
    import recipe
    if ingredients:
        recipes = recipe.get_recipes(ingredients=ingredients)
        for idx, recipe in enumerate(recipes, start=1):
            print(f"{idx}. {recipe['title']}")
            print(f"   Image: {recipe['image']}")
    else:
        recipes = ["Recipes not found; No ingridents found"]

    return render_template("result.html", recipes=recipes, enumerate=enumerate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
