document.addEventListener("DOMContentLoaded", function() {
    const rightScrollBtn = document.querySelector('.right-scroll');
    const leftScrollBtn = document.querySelector('.left-scroll');
    const categories = Array.from(document.querySelectorAll('.category')); // Усі категорії
    let visibleCount = getVisibleCount(); // Отримуємо кількість видимих категорій відповідно до ширини екрана
    let currentStartIndex = 0; // Індекс першої видимої категорії

    // Функція для отримання кількості видимих категорій
    function getVisibleCount() {
        const screenWidth = window.innerWidth;
        if (screenWidth < 600) {
            return 1; // На маленьких екранах показуємо 1 категорію
        } else if (screenWidth < 1024) {
            return 2; // На середніх екранах показуємо 2 категорії
        } else {
            return 4; // На великих екранах показуємо 4 категорії
        }
    }

    // Функція для оновлення видимих категорій
    function updateVisibleCategories() {
        categories.forEach((category, index) => {
            if (index >= currentStartIndex && index < currentStartIndex + visibleCount) {
                category.style.display = 'flex'; // Показуємо категорію
            } else {
                category.style.display = 'none'; // Ховаємо категорію
            }
        });

        // Оновлюємо видимість стрілок
        updateArrowVisibility();
    }

    // Оновлення видимості стрілок
    function updateArrowVisibility() {
        if (currentStartIndex === 0) {
            leftScrollBtn.style.display = 'none'; // Ховаємо ліву стрілку на початку
        } else {
            leftScrollBtn.style.display = 'block'; // Показуємо ліву стрілку
        }

        if (currentStartIndex + visibleCount >= categories.length) {
            rightScrollBtn.style.display = 'none'; // Ховаємо праву стрілку, якщо досягли кінця
        } else {
            rightScrollBtn.style.display = 'block'; // Показуємо праву стрілку
        }
    }

    // Оновлюємо кількість видимих категорій при зміні розміру вікна
    window.addEventListener('resize', function() {
        visibleCount = getVisibleCount(); // Оновлюємо visibleCount при зміні ширини екрана
        updateVisibleCategories();
    });

    // Натискання на праву стрілку
    rightScrollBtn.addEventListener('click', function() {
        // Перевіряємо, чи не досягли ми кінця категорій
        if (currentStartIndex + visibleCount < categories.length) {
            currentStartIndex++; // Зміщуємо індекс вправо
            updateVisibleCategories();
        }
    });

    // Натискання на ліву стрілку
    leftScrollBtn.addEventListener('click', function() {
        if (currentStartIndex > 0) {
            currentStartIndex--; // Зміщуємо індекс вліво
            updateVisibleCategories();
        }
    });

    // Початкова ініціалізація
    updateVisibleCategories();
});
