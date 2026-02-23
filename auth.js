const API = "http://localhost:8000";

async function login(username, password){
    const res = await fetch(API + "/api/auth/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    if(!res.ok){
        alert("Credenciais inválidas");
        return;
    }

    const data = await res.json();
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("role", data.role);

    if(data.role === "admin"){
        window.location.href = "admin.html";
    } else {
        window.location.href = "index.html";
    }
}

document.getElementById("loginForm").addEventListener("submit", e=>{
    e.preventDefault();
    login(username.value, password.value);
});

document.getElementById("adminQuick").onclick = ()=> login("admin","admin123");
document.getElementById("viewerQuick").onclick = ()=> login("user","user123");
