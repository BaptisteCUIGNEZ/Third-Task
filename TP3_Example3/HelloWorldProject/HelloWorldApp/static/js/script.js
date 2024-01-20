

document.addEventListener('DOMContentLoaded', function () {

    // Counter functionality
    var counterButton = document.getElementById('counterButton');
    var countElement = document.getElementById('count');
    var counter = 0;

    counterButton.addEventListener('click', function () {
        counter++;
        countElement.innerText = counter;
    });

    console.log('Hello, World! This is JavaScript.');
});
