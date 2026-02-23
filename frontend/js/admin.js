const API = "http://localhost:8000";

if(localStorage.getItem("role") !== "admin"){
    window.location.href = "login.html";
}

async function loadMeals(){
    const res = await fetch(API + "/api/meals/");
    const meals = await res.json();
    const container = document.getElementById("mealList");
    container.innerHTML = "";
    meals.forEach(m => {
        container.innerHTML += `<p>${m.name} - ${m.calories} kcal</p>`;
    });
}

document.getElementById("mealForm").addEventListener("submit", async e=>{
    e.preventDefault();
    await fetch(API + "/api/meals/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: mealName.value,
            calories: parseInt(mealCalories.value)
        })
    });
    mealName.value = "";
    mealCalories.value = "";
    loadMeals();
});

loadMeals();
