const express = require('express');
const app = express();

app.listen(3000, () => {console.log('Server is running on port 3000')});
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}));

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0], //3
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0], //6
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] //9
];
printBoard = () => {
    for (var i = 0; i < board.length; i++) {
        for (var j = 0; j < board[i].length; j++) {
            process.stdout.write(board[i][j] + ' ');
        }
        console.log('');
    }
}
app.post('/api/boardIn', (req, res) => {
    let {x, y, value} = req.body;
    board[y][x] = value;
    res.send("OK");
    console.clear();
    printBoard();
});
app.get('/api/boardOut', (req, res) => {
    res.send(board);
});
printBoard();