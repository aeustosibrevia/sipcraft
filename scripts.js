document.addEventListener("DOMContentLoaded", function() {
    const rightScrollBtn = document.querySelector('.right-scroll');
    const leftScrollBtn = document.querySelector('.left-scroll');
    const categories = Array.from(document.querySelectorAll('.category')); 
    let visibleCount = getVisibleCount(); 
    let currentStartIndex = 0; 

      function getVisibleCount() {
        const screenWidth = window.innerWidth;
        if (screenWidth < 600) {
            return 1; 
        } else if (screenWidth < 1024) {
            return 2; 
        } else {
            return 4; 
        }
    }

    function updateVisibleCategories() {
        categories.forEach((category, index) => {
            if (index >= currentStartIndex && index < currentStartIndex + visibleCount) {
                category.style.display = 'flex';
            } else {
                category.style.display = 'none'; 
            }
        });

        updateArrowVisibility();
    }

    function updateArrowVisibility() {

        if (currentStartIndex === 0) {
            leftScrollBtn.style.display = 'none'; 
        } else {
            leftScrollBtn.style.display = 'block'; 
        }
        if (currentStartIndex + visibleCount >= categories.length) {
            rightScrollBtn.style.display = 'none';

        } else {
            rightScrollBtn.style.display = 'block'; 
        }
    }

 
    window.addEventListener('resize', function() {
        visibleCount = getVisibleCount();
        updateVisibleCategories();
    });

    rightScrollBtn.addEventListener('click', function() {
        if (currentStartIndex + visibleCount < categories.length) {
            currentStartIndex++;
            updateVisibleCategories();
        }
    });

    leftScrollBtn.addEventListener('click', function() {
        if (currentStartIndex > 0) {
            currentStartIndex--; 
            updateVisibleCategories();
        }
    });

    updateVisibleCategories();
});
