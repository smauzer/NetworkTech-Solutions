let valueDisplays = document.querySelectorAll(".num");

function count_up() {
    valueDisplays.forEach((valueDisplay) => {
        let startValue = 0;
        let endValue = parseInt(valueDisplay.getAttribute("data-val"));
        let interval = parseInt(valueDisplay.getAttribute("data-interval"));
        let duration = Math.floor(interval / endValue);
        let counter = setInterval(function () {
            startValue += 1;
            valueDisplay.textContent = startValue;
            if (startValue == endValue) {
                clearInterval(counter);
            }
        }, duration);
    });
}

const targetElement = document.querySelector('.counter-cont');

// Create a new Intersection Observer
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        // If the element is in the viewport
        if (entry.isIntersecting) {
        // Call your function here
        count_up();
        // Unobserve the element so the function is only called once
        observer.unobserve(entry.target);
        }
    });
});

// Start observing the target element
observer.observe(targetElement);