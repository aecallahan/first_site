// Hacky frontend utility functions until I change this to use a restful JS framework

var TOTAL_PICTURES = 4;

var imagePath = function() {
    var number = Math.floor(Math.random() * TOTAL_PICTURES);
    return number;
}
