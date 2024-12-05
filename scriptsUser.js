document.addEventListener('DOMContentLoaded', () => {
    const userIcon = document.getElementById('userIcon');
    const userPopup = document.getElementById('userPopup');
    const usernameDisplay = document.getElementById('usernameDisplay'); 
    const userInfo = document.getElementById('userInfo'); 
    const separator = document.getElementById('separator'); 
    const loginBtn = document.getElementById('loginBtn'); 
    const registerBtn = document.getElementById('registerBtn'); 
    const logoutBtn = document.getElementById('logoutBtn'); 

    let isLoggedIn = true;
    let username = "Іван Іваненко";

    function updatePopupContent() {
        if (isLoggedIn) {
            usernameDisplay.textContent = username;
            usernameDisplay.classList.remove('hidden');
            userInfo.classList.remove('hidden');
            separator.classList.remove('hidden');
            loginBtn.classList.add('hidden');
            registerBtn.classList.add('hidden');
            logoutBtn.classList.remove('hidden');
        } else {
            popupMessage.textContent = "Ви ще не увійшли у акаунт";
            usernameDisplay.classList.add('hidden');
            userInfo.classList.add('hidden');
            separator.classList.add('hidden');
            loginBtn.classList.remove('hidden');
            registerBtn.classList.remove('hidden');
            logoutBtn.classList.add('hidden');
        }
    }

    userIcon.addEventListener('click', () => {
        userPopup.classList.toggle('hidden');
        updatePopupContent();
    });

    loginBtn.addEventListener('click', () => {
        window.location.href = "login.html";
    });

    registerBtn.addEventListener('click', () => {
        window.location.href = "singup.html"; 
    });

    logoutBtn.addEventListener('click', () => {
        isLoggedIn = false;
        alert("Ви вийшли з акаунта!");
        updatePopupContent();
    });

    window.addEventListener('click', (e) => {
        if (!userPopup.contains(e.target) && e.target !== userIcon) {
            userPopup.classList.add('hidden');
        }
    });
});


