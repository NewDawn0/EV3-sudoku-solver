async function postData (x, y, value) {
    const response = await fetch('/api/boardIn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({x, y, value})
    });
    return response.json();
}
var numSelected = null;
var tileSelected = null;
var board = [
    "---------",
    "---------",
    "---------",
    "---------",
    "---------",
    "---------",
    "---------",
    "---------",
    "---------"
]
window.onload = function() {
    clearBoard();
    setGame();
}
clearBoard = () => {
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            postData(c, r, 0);
        }
    }
};
function setGame() {
    // Digits 1-9
    for (let i = 1; i <= 9; i++) {
        //<div id="1" class="number">1</div>
        let number = document.createElement("div");
        number.id = i
        number.innerText = i;
        number.addEventListener("click", selectNumber);
        number.classList.add("number");
        document.getElementById("digits").appendChild(number);
    }
    // Board 9x9
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            let tile = document.createElement("div");
            tile.id = r.toString() + "-" + c.toString();
            if (board[r][c] != "-") {
                tile.innerText = board[r][c];
                tile.classList.add("tile-start");
            }
            tile.addEventListener("click", selectTile);
            tile.classList.add("tile");
            document.getElementById("board").append(tile);
        }
    }
}
function selectNumber(){
    if (numSelected != null) {
        numSelected.classList.remove("number-selected");
    }
    numSelected = this;
    numSelected.classList.add("number-selected");
}
function selectTile() {
    if (numSelected) {
        this.innerText = numSelected.innerText;
        x = parseInt(this.id.split("-")[1]);
        y = parseInt(this.id.split("-")[0]);
        value = parseInt(numSelected.innerText);
        postData(x, y, value);
    }
}
