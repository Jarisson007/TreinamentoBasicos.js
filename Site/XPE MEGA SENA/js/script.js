var state = {board: [], currentGame: [], savedGames: [] };

function start() {
    addNumberToGame(1);
    addNumberToGame(2);
    addNumberToGame(3);
    addNumberToGame(4);
    addNumberToGame(5);

    console.log(state.currentGame);
}

function addNumberToGame(numberToAdd) {
    if (numberToAdd <1 || numberToAdd > 60){
    state.currentGame.push(numberToAdd);
    return;
}

    if (state.currentGame.length >= 6) {
        console.error('O jogo já está completo.');
    }

    state.currentGame.push(numberToAdd);
}
start();