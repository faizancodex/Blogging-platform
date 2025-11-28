console.log("script.js loaded and running");

// for scroller menu
const scrollAmount = 300;
const scroller = document.getElementById('scroller');
const scrollLeftButton = document.getElementById('scrollLeftButton');
const scrollRightButton = document.getElementById('scrollRightButton');

function updateButtonVisibility() {
    // if (!scroller || !scrollLeftButton || !scrollRightButton) return;
    const maxScrollLeft = scroller.scrollWidth - scroller.clientWidth;
    scrollLeftButton.classList.toggle('hidden', scroller.scrollLeft === 0);
    scrollRightButton.classList.toggle('hidden', scroller.scrollLeft >= maxScrollLeft);
}


if (scrollRightButton && scrollLeftButton && scroller) {
    scrollRightButton.addEventListener('click', function () {
        scroller.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        updateButtonVisibility();
    });

    scrollLeftButton.addEventListener('click', function () {
        scroller.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        updateButtonVisibility();
    });

    scroller.addEventListener('scroll', updateButtonVisibility);

    // Initial check
    updateButtonVisibility();
}


// for form password
const forms = document.querySelector(".account_form"),
    pwShowHide = document.querySelectorAll(".pw-eye"),
    links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");

        pwFields.forEach(password => {
            if (password.type === "password") {
                // Show password
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            // Hide password
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        })

    })
})


