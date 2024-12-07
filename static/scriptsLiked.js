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
                } else {
                    alert(result.message || 'An error occurred.');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });
});