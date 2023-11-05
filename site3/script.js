const navbarMenu = document.querySelector(".navbar .links");
const hamburgerBtn = document.querySelector(".hamburger-btn");
const hideMenuBtn = navbarMenu.querySelector(".close-btn");
const showPopupBtn = document.querySelector(".login-btn");
const formPopup = document.querySelector(".form-popup");
const hidePopupBtn = formPopup.querySelector(".close-btn");
const signupLoginLink = formPopup.querySelectorAll(".bottom-link a");

var semBlock = document.getElementById("sem-block")
var eventsBlock = document.getElementById("events-block")
var thesesBlock = document.getElementById("theses-block")

var semButton = document.getElementById("sem-button")
var eventsButton = document.getElementById("events-button")
var thesesButton = document.getElementById("theses-button")

semButton.sem-container.display = 'none'
eventsButton.sem-container.display = 'none'
thesesButton.sem-container.display = 'none'

// Show mobile menu
hamburgerBtn.addEventListener("click", () => {
    navbarMenu.classList.toggle("show-menu");
});

// Hide mobile menu
hideMenuBtn.addEventListener("click", () =>  hamburgerBtn.click());

// Show login popup
showPopupBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-popup");
});

// Hide login popup
hidePopupBtn.addEventListener("click", () => showPopupBtn.click());

// Show or hide signup form
signupLoginLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        formPopup.classList[link.id === 'signup-link' ? 'add' : 'remove']("show-signup");
    });
});

semButton.addEventListener("click", () => {
    semBlock.sem-container.display = 'block';
    eventsBlock.sem-container.display = 'none';
    thesesBlock.sem-container.display = 'none';
});

eventsButton.addEventListener("click", () => {
    semBlock.sem-container.display = 'none';
    eventsBlock.sem-container.display = 'block';
    thesesBlock.sem-container.display = 'none';
});

thesesButton.addEventListener("click", () => {
    semBlock.sem-container.display = 'none';
    eventsBlock.sem-container.display = 'none';
    thesesBlock.sem-container.display = 'block';
});
