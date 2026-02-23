const API = "http://localhost:8000";

async function loadMeals(){
    const res = await fetch(API + "/api/meals/");
    const meals = await res.json();
    const container = document.getElementById("meals");
    container.innerHTML = "";
    meals.forEach(m => {
        container.innerHTML += `<p>${m.name} - ${m.calories} kcal</p>`;
    });
}

loadMeals();
