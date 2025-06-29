# Game
### Connect 4 AI 

Connect 4 is a classic game where two players take turns dropping colored discs into a grid. **The goal?** Be the first to connect four of your discs **horizontally**, **vertically**, or **diagonally**. This AI-powered version utilizes algorithms like minimax and alpha-beta pruning to analyze moves and make strategic decisions. 
> Play against the computer and challenge its intelligent gameplay!

### How It Works

This AI-powered Connect 4 game uses algorithms to predict and select the best moves based on the current game state. The minimax algorithm evaluates possible moves, considering potential future scenarios, while alpha-beta pruning optimizes the search, narrowing down the most promising paths. The AI calculates the best move by maximizing its chances of winning and minimizing the opponent's possibilities, providing a challenging and enjoyable gaming experience.


### Alpha Beta Pruning

Alpha-beta pruning in Connect 4 involves discarding irrelevant game branches while exploring possible moves. It evaluates the game state by assigning alpha (the best value for the maximizing player) and beta (the best value for the minimizing player). By disregarding unpromising moves, it significantly reduces the number of nodes analyzed, optimizing the AI's decision-making process and improving computational efficiency.
<img src="./assets/minimax with alpha beta pruning .jpg">


### Pseudocode
```
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth == 0 or node is terminal then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            if value > β then
                break (* β cutoff *)
            α := max(α, value)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            if value < α then
                break (* α cutoff *)
            β := min(β, value)
        return value
```

### Comparison between Minimax and Minimax with Alpha Beta Pruning

<img src="./assets/Comparison M vs MAP.jpg">

## Source
[Alpha beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
[Minimax algorithm and alpha-beta pruning](https://medium.com/@aaronbrennan.brennan/minimax-algorithm-and-alpha-beta-pruning-646beb01566c)
[Connect -4](http://www-personal.engin.umd.umich.edu/~shaout/connect4.pdf)

