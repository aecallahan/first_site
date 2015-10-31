var global = {};
$(document).ready(function() {
    newGame();
    $('.game').on('click', '.column', function() {
        play($(this));
    });
    // Create a Spinner with options
    var spinner = new Spinner({
        scale: 3, // Multiply the spinner's size
        lines: 12, // The number of lines to draw
        length: 7, // The length of each line
        width: 5, // The line thickness
        radius: 10, // The radius of the inner circle
        color: '#FFFF00', // #rbg or #rrggbb
        speed: 1, // Rounds per second
        trail: 100, // Afterglow percentage
        shadow: true // Whether to render a shadow
    }).spin(document.getElementById("loading")); // Place in DOM node called "loading"
});


// Constants
var RED = 'red',
    BLACK = 'black',
    VICTORY = 'victory',
    ORIGINAL_TITLE = 'Connect Three',
    RED_TITLE = 'Red won!',
    BLACK_TITLE = 'Black won!',
    DRAW_TITLE = "It's a Draw",
    PLEASE_WAIT = "Calculating, please wait...",
    BOARD_HEIGHT = 4,
    BOARD_WIDTH = 4,
    WIN_LENGTH = 3,
    DEFAULT_BOARD = [[],[],[],[],],
    MAX_DEPTH = 100000;


// Variables
var currentID = 0,
    depth = 0;


var play = function(column) {
    var game = global.game;
    if (game.isOver) {
        if (confirm('Would you like to play again?')) newGame();
    } else {
        var columnIndex = column.attr('id')[3];
        if (game.getAvailableMoves().indexOf(parseInt(columnIndex)) != -1) {
            colorBoard(columnIndex);
            game.makeMove(columnIndex);
            if (game.isOver) {
                colorVictory();
                changeTitle();
            } else if (game.activePlayer == BLACK) {
                $('.warning').show();
                setTimeout(function() {
                    var botColumn = botChooseColumn();
                    play(botColumn);
                    $('.warning').hide();
                }, 500);
            }
        }
    }
}


// Change the page's title to reflect game state
var changeTitle = function() {
    var game = global.game;
    if (game.isOver) {
        if (game.isDraw) {
            $('h1').text(DRAW_TITLE);
        } else if (game.activePlayer == RED) {
            $('h1').text(RED_TITLE);
        } else {
            $('h1').text(BLACK_TITLE);
        }
    } else $('h1').text(ORIGINAL_TITLE);
}


// Color the board to match a play being made
var colorBoard = function(columnIndex) {
    var game = global.game;
    var column = $('#col' + columnIndex);
    var slot = column.find('.' + game.board[columnIndex].length);
    slot.addClass(game.activePlayer);
}


// Color the winning set of pieces
var colorVictory = function() {
    var game = global.game;
    if (game.isDraw) {
        return;
    }
    var currentCoords = game.winningPiece;
    for (var i = 0; i < WIN_LENGTH; i++) {
        $('#col' + currentCoords[0]).find('.' + currentCoords[1]).addClass(VICTORY);
        currentCoords[0] += game.winningVector[0];
        currentCoords[1] += game.winningVector[1];
    }
}


// Clear the board for a new game
var newGame = function() {
    global.game = new Game([[],[],[],[],], BLACK);
    changeTitle();

    // Clear all classes added during gameplay
    $('.circle').removeClass(RED);
    $('.circle').removeClass(BLACK);
    $('.circle').removeClass(VICTORY);

    botFirstTurn();
}


// Make black always move first and pick randomly
var botFirstTurn = function() {
    var column = Math.floor(Math.random() * BOARD_WIDTH);
    colorBoard(column);
    global.game.makeMove(column);
}


// Black chooses where to play
var botChooseColumn = function() {
    var game = global.game;
    depth = 0;
    miniMax(game);
    var move = game.miniMaxBlackChoice;
    return $('#col' + move);
}


// Return the score of a game depending on its outcome
var score = function(game) {
    if (game.isOver && game.activePlayer == BLACK) {
        return 1;
    } else if (game.isOver && game.activePlayer == RED) {
        return -1;
    } else {
        return 0;
    }
}


var miniMax = function(game) {
    // depth++;
    if (game.isOver || depth > MAX_DEPTH) return score(game);
    var scores = [];
    var moves = [];

    var availableMoves = game.getAvailableMoves();
    for (var i = 0; i < availableMoves.length; i++) {
        var possibleGame = game.copy();
        possibleGame.makeMove(availableMoves[i]);
        scores.push(miniMax(possibleGame));
        moves.push(availableMoves[i]);
    }


    if (game.activePlayer == BLACK) {
        // Return the move with the max score
        var maxScoreIndex = scores.indexOf(scores.max());
        if (maxScoreIndex == -1) maxScoreIndex = Math.floor(Math.random() * scores.length);
        global.game.miniMaxBlackChoice = moves[maxScoreIndex];
        if (moves[maxScoreIndex] == -1) debugger;
        return scores[maxScoreIndex];
    } else {
        // Return the move with the min score
        var minScoreIndex = scores.indexOf(scores.min());
        if (minScoreIndex == -1) minScoreIndex = Math.floor(Math.random() * scores.length);
        global.game.miniMaxRedChoice = moves[minScoreIndex];
        return scores[minScoreIndex];
    }
}


// DEFINE THE GAME OBJECT
var Game = function(board, activePlayer) {
    this.id = currentID;
    this.board = board;
    this.activePlayer = activePlayer;
    this.isOver = false;
    this.isDraw = false;
    this.winningPiece = [];
    this.winningVector = [];
    this.miniMaxRedChoice = -1;
    this.miniMaxBlackChoice = -1;
    currentID++;
}


Game.prototype = {
    // Return an array with the indices of all columns are not full
    getAvailableMoves: function() {
        var moves = [];
        for (var i = 0; i < this.board.length; i++) {
            if (this.board[i].length < BOARD_HEIGHT) moves.push(i);
        }
        return moves;
    },
    // Make a particular move
    makeMove: function(column) {
        this.board[column].push(this.activePlayer);
        if (this.checkIfWon(column)) {
            this.isOver = true;
        } else if (!this.getAvailableMoves().length) {
            this.isOver = true;
            this.isDraw = true;
        } else {
            this.switchPlayer();
        }
    },
    // Check if the last move ended the game
    checkIfWon: function(column) {
        column = parseInt(column);
        var row = this.board[column].length - 1;
        var adjacentSlots = this.getAdjacentSlots(column, row);
        for (var i = 0; i < adjacentSlots.length; i++) {
            if (this.checkConnectedLength([column, row], adjacentSlots[i])) return true;
        }
        return false;
    },
    // Retrieve half of the positions touching a given position
    getAdjacentSlots: function(column, row) {
        var adjacentSlots= [];
        adjacentSlots.push([column -1, row]);
        adjacentSlots.push([column - 1, row - 1]);
        adjacentSlots.push([column, row - 1]);
        adjacentSlots.push([column + 1, row - 1]);

        return adjacentSlots;
    },
    // Given two adjacent positions, check if these positions are
    // part of a set of matching positions long enough to win
    checkConnectedLength: function(newestCoords, adjacentCoords) {
        var connectedLength = 1;
        // Compute the vector from one coordinate to the other
        var differenceVector = [adjacentCoords[0] - newestCoords[0], adjacentCoords[1] - newestCoords[1]];
        var currentCoords = adjacentCoords;
        while (this.isActiveColor(currentCoords[0], currentCoords[1])) {
            connectedLength++;
            if (connectedLength >= WIN_LENGTH) {
                this.winningPiece = newestCoords;
                this.winningVector = differenceVector;
                return true;
            }
            currentCoords[0] += differenceVector[0];
            currentCoords[1] += differenceVector[1];
        }
        // After looking in one direction for a match, look in the other direction
        currentCoords[0] = newestCoords[0] - differenceVector[0];
        currentCoords[1] = newestCoords[1] - differenceVector[1];
        while (this.isActiveColor(currentCoords[0], currentCoords[1])) {
            connectedLength++;
            if (connectedLength >= WIN_LENGTH) {
                this.winningPiece = currentCoords;
                this.winningVector = differenceVector;
                return true;
            }
            currentCoords[0] -= differenceVector[0];
            currentCoords[1] -= differenceVector[1];
        }
        return false;
    },
    // Check if a position is owned by the active player
    isActiveColor: function(column, row) {
        // Handle requests for slots that are not on the board
        if (column < 0 || row < 0) return false;
        if (column >= this.board.length) return false;
        if (row >= this.board[column].length) return false;

        return this.board[column][row] == this.activePlayer;
    },
    switchPlayer: function() {
        this.activePlayer = (this.activePlayer === RED) ? BLACK : RED;
    },
    copy: function() {
        var boardCopy = copyBoard(this.board);
        var newGame = new Game(boardCopy, this.activePlayer);
        return newGame;
    },
}


var copyBoard = function(board) {
    var boardCopy = []
    for (var i = 0; i < board.length; i++) {
        boardCopy.push(board[i].slice());
    }
    return boardCopy;
}


Array.prototype.max = function() {
    return Math.max.apply(null, this);
}

Array.prototype.min = function() {
    return Math.min.apply(null, this);
}
