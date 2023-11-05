var semBlock = document.getElementById("sem-block")
var eventsBlock = document.getElementById("events-block")
var thesesBlock = document.getElementById("theses-block")

var semButton = document.getElementById("sem-button")
var eventsButton = document.getElementById("events-button")
var thesesButton = document.getElementById("theses-button")

semBlock.style.display = 'none'
eventsBlock.style.display = 'none'
thesesBlock .style.display = 'none'

semButton.addEventListener("click", () => {
    semBlock.style.display = 'block';
    eventsBlock.style.display = 'none';
    thesesBlock.style.display = 'none';
});

eventsButton.addEventListener("click", () => {
    semBlock.style.display = 'none';
    eventsBlock.style.display = 'block';
    thesesBlock.style.display = 'none';
});

thesesButton.addEventListener("click", () => {
    semBlock.style.display = 'none';
    eventsBlock.style.display = 'none';
    thesesBlock.style.display = 'block';
});
