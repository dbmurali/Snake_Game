# Snake Game

This is a classic Snake game built using Python and the `turtle` graphics library. In this game, the player controls a snake that grows longer as it eats food. The objective is to eat as much food as possible without running into the walls or the snake’s own tail.

## Features:
- **Snake Movement**: The snake moves in four directions: up, down, left, and right, using keyboard arrow keys.
- **Food Collection**: The snake eats food and grows longer each time it consumes food.
- **Score Display**: The score increases as the snake eats food, and the score is displayed at the top of the screen.
- **Game Over**: The game ends when the snake runs into the wall or its own tail.
- **Restart Option**: The game can be played again after it ends by simply restarting the program.


## Game Instructions:
- Left Arrow Key: Move the snake left.
- Right Arrow Key: Move the snake right.
- Up Arrow Key: Move the snake up.
- Down Arrow Key: Move the snake down.
- The objective of the game is to eat the food (represented by a square) to grow the snake and increase your score.
- The game ends if the snake hits the wall or runs into itself.

### Code Breakdown:  
- Main Game Loop (main.py):
  The main script where the game is set up, and the game loop runs. It creates the window, controls the snake and food, and updates the game state.

- Snake Class (snake.py):
  This class handles the creation and movement of the snake, as well as the logic to extend the snake when it eats food.

- Food Class (food.py):
  The food class generates new food at random positions on the screen. The snake eats this food to grow and increase the score.

- Scoreboard Class (scoreboard.py):
  The scoreboard class is responsible for keeping track of the score and displaying it on the screen. It also handles the "Game Over" screen.

## Screenshots:
### 1. **Game in Action**:
   ![Game Screenshot](https://github.com/dbmurali/Snake_Game/blob/7d58b679d220ffd9c123b56be0d483ca7825a939/start%20game.png)

### 2. **Game Over**:
   ![Game over](https://github.com/dbmurali/Snake_Game/blob/7d58b679d220ffd9c123b56be0d483ca7825a939/snake%20game%20over.png)

## Requirements:
To run this game, you need Python installed on your computer. The following libraries are required:
- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
- **turtle**: The `turtle` graphics library is used for creating the game’s user interface. It is pre-installed with Python, so no additional installation is required.

## How to Run:
1. Ensure that Python 3.x is installed on your computer.
2. Download or clone this repository to your local machine.
3. Navigate to the project directory in the terminal/command prompt.
4. Run the game by executing:
   ```bash
   python main.py
