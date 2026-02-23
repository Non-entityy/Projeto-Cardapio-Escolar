//const API = "http://localhost:8000";
const API = "https://ideal-fiesta-97ww64jgxw5w37q96-8000.app.github.dev/";

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
