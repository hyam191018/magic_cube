# RubikCube Solver

## Overview
This project provides a Python implementation of a 3x3 Rubik's Cube simulator with the ability to scramble, restore, and solve the cube using the `rubik.cube` and `rubik.solve` libraries.

## Features
- **Cube Representation:** Represents the cube using a dictionary with six faces (U, D, L, R, F, B).
- **Random Scrambling:** Scrambles the cube with a series of random moves.
- **Rotation Methods:** Implements rotation logic for all possible moves (U, D, L, R, F, B and their variations).
- **State Display:** Prints the cube's current state.
- **Solver Integration:** Uses `rubik.solve` to find and apply the optimal solution.

## Installation
Ensure you have Python installed and install the required dependencies:
```bash
pip install rubik
```

## Usage
```python
from rubik_cube import RubikCube

cube = RubikCube()
cube.show()  # Display the initial state

cube.scramble(20)  # Scramble the cube with 20 random moves
cube.show()

cube.solver()  # Solve the cube
cube.show()
```

## Class: `RubikCube`
### Methods
- `show()`: Displays the current cube state.
- `scramble(run=10000)`: Scrambles the cube with a given number of random moves.
- `restore()`: Restores the cube to its original state.
- `solver()`: Uses an external solver to find the solution.
- `test()`: Tests all possible moves.

## Enum: `Move`
Defines all 18 possible moves, including clockwise, counterclockwise, and double turns.

## License
This project is open-source and available for modification and distribution.

