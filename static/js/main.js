const ingredients = [];

function addIngredient() {
    const inputField = document.getElementById("ingredient-input");
    const ingredient = inputField.value.trim();

    if (ingredient) {
        ingredients.push(ingredient);
        updateIngredientList();
        inputField.value = "";
    } else {
        alert("Please enter a valid ingredient.");
    }
}

function updateIngredientList() {
    const listElement = document.getElementById("ingredients-list");
    listElement.innerHTML = "";

    ingredients.forEach((ing, index) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${index + 1}. ${ing}`;
        listElement.appendChild(listItem);
    });
}

//<script src="{{ url_for('static', filename='js/main.js') }}"></script>