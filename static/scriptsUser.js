document.addEventListener("DOMContentLoaded", () => {
    const userIcon = document.querySelector("nav ul li:nth-child(5) a img");
    const popup = document.getElementById("userPopup");
    const popupMessage = document.getElementById("popupMessage");
    const loginBtn = document.getElementById("loginBtn");
    const registerBtn = document.getElementById("registerBtn");
    const logoutBtn = document.getElementById("logoutBtn");
    const usernameDisplay = document.getElementById("usernameDisplay");
    const userInfo = document.getElementById("userInfo");
    const separator = document.getElementById("separator");

    fetch("/api/auth_status")
        .then((response) => response.json())
        .then((data) => {
            if (data.isLoggedIn) {
                showLoggedInView(data.username);
            } else {
                showLoggedOutView();
            }
        })
        .catch((error) => {
            console.error("Error fetching auth status:", error);
        });

    userIcon.addEventListener("click", (event) => {
        event.preventDefault();
        popup.classList.toggle("hidden");
    });

    function showLoggedInView(username) {
        popupMessage.classList.add("hidden");
        loginBtn.classList.add("hidden");
        registerBtn.classList.add("hidden");

        usernameDisplay.textContent = username;
        usernameDisplay.classList.remove("hidden");
        separator.classList.remove("hidden");
        userInfo.textContent = `Вітаємо, ${username}!`;
        userInfo.classList.remove("hidden");

        logoutBtn.classList.remove("hidden");
    }

    function showLoggedOutView() {
        popupMessage.textContent = "Ви ще не увійшли у акаунт";
        popupMessage.classList.remove("hidden");

        loginBtn.classList.remove("hidden");
        registerBtn.classList.remove("hidden");

        usernameDisplay.classList.add("hidden");
        separator.classList.add("hidden");
        userInfo.classList.add("hidden");

        logoutBtn.classList.add("hidden");
    }

    loginBtn.addEventListener("click", () => {
        window.location.href = "/login";
    });

    registerBtn.addEventListener("click", () => {
        window.location.href = "/signup";
    });

    logoutBtn.addEventListener("click", () => {
        fetch("/logout")
            .then(() => {
                showLoggedOutView();
            })
            .catch((error) => {
                console.error("Error logging out:", error);
            });
    });

    document.addEventListener("click", (event) => {
        if (!popup.contains(event.target) && event.target !== userIcon) {
            popup.classList.add("hidden");
        }
    });
});
