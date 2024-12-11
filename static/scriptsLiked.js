document.addEventListener('DOMContentLoaded', () => {
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            event.preventDefault();

            const likeIcon = button.querySelector('.like-icon');
            const isLiked = likeIcon.getAttribute('data-liked') === 'true';
            const form = button.closest('form');
            const actionUrl = form.action;

            try {
                const response = await fetch(actionUrl, {method: 'POST'});
                const result = await response.json();

                if (result.success) {
                    likeIcon.src = result.liked
                        ? '/static/picture/header/likedPaint.png'
                        : '/static/picture/header/liked.png';
                    likeIcon.setAttribute('data-liked', result.liked.toString());
                    showToast(result.message || 'Товар додано до улюблених.', 'success');
                } else {
                    showToast(result.message || 'Сталась помилка.', 'error');
                }
            } catch (error) {
                console.error('Error:', error);
                showToast('An unexpected error occurred.', 'error');
            }
        });
    });
});

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