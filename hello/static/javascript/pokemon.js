// Hacky frontend utility functions until I change this to use a restful JS framework

$(document).ready(function() {
    // Disable enter key
    $('html').bind('keypress', function(e) {
        code = e.keyCode || e.which;
       if (code == 13) {
          e.preventDefault();
          return false;
       }
    });

    // Auto-submit the form when the correct answer has been entered
    $('#pokemon-name').on('input', function() {
        if ($(this).val().toLowerCase() == pokemonName) {
            document.getElementById('poke-form').submit();
        }
    });
});


var display = document.getElementById('timer');
startTimer(5, display);


function startTimer(duration, display) {
    setInterval(function () {
        display.textContent = duration;

        if (--duration < 0) {
            document.getElementById('poke-form').submit();
        }
    }, 1000);
}
