// Hacky frontend utility functions until I change this to use a restful JS framework

checkAnswer = function() {
    if (input.value.toLowerCase() == pokemonName) {
        document.getElementById('poke-form').submit();
    }
};

var input = document.getElementById('pokemon-name');
input.oninput = checkAnswer;


var display = document.getElementById('timer');
startTimer(5, display);


function startTimer(duration, display) {
    setInterval(function () {
        display.textContent = duration;

        if (--duration < 0) {
            // display.textContent = "time's up!";
            document.getElementById('poke-form').submit();
        }
    }, 1000);
}
