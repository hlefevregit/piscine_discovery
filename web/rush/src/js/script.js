document.addEventListener("DOMContentLoaded", function() {
    // Loader
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });

    // Smooth Scroll
    const navLinks = document.querySelectorAll('.nav-link');
    for (const link of navLinks) {
        link.addEventListener('click', smoothScroll);
    }

    function smoothScroll(event) {
        event.preventDefault();
        const targetId = event.currentTarget.getAttribute("href");
        const targetElement = document.querySelector(targetId);
        window.scrollTo({
            top: targetElement.offsetTop,
            behavior: "smooth"
        });
    }

    // Initialize AOS
    AOS.init();
});
