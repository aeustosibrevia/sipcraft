function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span>${message}</span>
        <div class="progress-bar"></div>
    `;
    document.body.appendChild(toast);

    const progressBar = toast.querySelector('.progress-bar');
    setTimeout(() => progressBar.style.width = '100%', 100);

    setTimeout(() => toast.remove(), 4000);
}

document.querySelectorAll('form[action^="/add_to_cart/"]').forEach(form => {
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const actionUrl = form.action;

        try {
            const response = await fetch(actionUrl, {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (response.ok) {
                showToast(result.message, 'success');
            } else {
                showToast(result.message, 'error');
            }
        } catch (error) {
            showToast('Сталася помилка. Спробуйте ще раз.', 'error');
        }
    });
});

const style = document.createElement('style');
style.innerHTML = `
.toast {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #333;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    margin-top: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.3s ease-out;
    display: flex;
    flex-direction: column;
    max-width: 300px;
}
.toast-success { background: #28a745; }
.toast-error { background: #dc3545; }
.progress-bar {
    height: 4px;
    width: 0;
    background: rgba(255, 255, 255, 0.8);
    transition: width 3.9s linear;
    margin-top: 5px;
}
`;
document.head.appendChild(style);