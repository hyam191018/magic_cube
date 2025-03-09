import random
from enum import Enum
from rubik.cube import Cube
from rubik.solve import Solver

class Move(Enum):
    U, U2, Ui, D, D2, Di, L, L2, Li, R, R2, Ri, F, F2, Fi, B, B2, Bi = range(18)

CLOCKWISE = 0
COUNTERCLOCKWISE = 1

class RubikCube:
    def __init__(self):
        self.length = 3
        self.colors = ["O", "R", "Y", "G", "W", "B"]
        self.faces = ["U", "D", "L", "R", "F", "B"]
        # matrix, i thought string is better ...
        self.state = {face: [[color] * self.length for _ in range(self.length)] for face, color in zip(self.faces, self.colors)}

    def show(self):
        print("\n>> Current Cube State:")
        for row in self.state["U"]:
            print("      " + " ".join(row))
        for i in range(self.length):
            print(" ".join(self.state["L"][i]) + " " + " ".join(self.state["F"][i]) + " " + " ".join(self.state["R"][i]) + " " + " ".join(self.state["B"][i]))
        for row in self.state["D"]:
            print("      " + " ".join(row))
        print()
    
    def __rotate(self, move):
        if move not in Move._value2member_map_:
            return

        def face_rotate(face, direction):
            if direction == CLOCKWISE:
                self.state[face] = [list(row) for row in zip(*self.state[face][::-1])]
            else:
                self.state[face] = [list(row) for row in zip(*self.state[face])][::-1]
        
        times = move % 3 + 1  # 1 for normal, 2 for double, 3 for inverse
        
        if move in {Move.U.value, Move.U2.value, Move.Ui.value}: 
            affected_faces = ["L", "F", "R", "B"]
            row = 0
            for _ in range(times):
                face_rotate("U", CLOCKWISE)
                self.state[affected_faces[0]][row], self.state[affected_faces[1]][row], self.state[affected_faces[2]][row], self.state[affected_faces[3]][row] = (
                    self.state[affected_faces[1]][row], self.state[affected_faces[2]][row], self.state[affected_faces[3]][row], self.state[affected_faces[0]][row]
                )
        
        elif move in {Move.D.value, Move.D2.value, Move.Di.value}: 
            affected_faces = ["L", "F", "R", "B"]
            row = 2
            for _ in range(times):
                face_rotate("D", CLOCKWISE)
                self.state[affected_faces[0]][row], self.state[affected_faces[1]][row], self.state[affected_faces[2]][row], self.state[affected_faces[3]][row] = (
                    self.state[affected_faces[3]][row], self.state[affected_faces[0]][row], self.state[affected_faces[1]][row], self.state[affected_faces[2]][row]
                )
        
        elif move in {Move.L.value, Move.L2.value, Move.Li.value}: 
            affected_faces = ["U", "F", "D", "B"]
            col = 0
            for _ in range(times):
                face_rotate("L", CLOCKWISE)
                for i in range(3):
                    self.state[affected_faces[0]][i][col], self.state[affected_faces[1]][i][col], self.state[affected_faces[2]][i][col], self.state[affected_faces[3]][2 - i][2] = (
                        self.state[affected_faces[3]][2 - i][2], self.state[affected_faces[0]][i][col], self.state[affected_faces[1]][i][col], self.state[affected_faces[2]][i][col]
                    )
        
        elif move in {Move.R.value, Move.R2.value, Move.Ri.value}: 
            affected_faces = ["U", "F", "D", "B"]
            col = 2
            for _ in range(times):
                face_rotate("R", CLOCKWISE)
                for i in range(3):
                    self.state[affected_faces[0]][i][col], self.state[affected_faces[1]][i][col], self.state[affected_faces[2]][i][col], self.state[affected_faces[3]][2 - i][0] = (
                        self.state[affected_faces[1]][i][col], self.state[affected_faces[2]][i][col], self.state[affected_faces[3]][2 - i][0], self.state[affected_faces[0]][i][col]
                    )
        
        elif move in {Move.F.value, Move.F2.value, Move.Fi.value}: 
            affected_faces = ["U", "L", "D", "R"]
            for _ in range(times):
                face_rotate("F", CLOCKWISE)
                for i in range(3):
                    self.state[affected_faces[0]][2][i], self.state[affected_faces[1]][2 - i][2], self.state[affected_faces[2]][0][2 - i], self.state[affected_faces[3]][i][0] = (
                        self.state[affected_faces[1]][2 - i][2], self.state[affected_faces[2]][0][2 - i], self.state[affected_faces[3]][i][0], self.state[affected_faces[0]][2][i], 
                    )
        
        elif move in {Move.B.value, Move.B2.value, Move.Bi.value}: 
            affected_faces = ["U", "L", "D", "R"]
            for _ in range(times):
                face_rotate("B", CLOCKWISE)
                for i in range(3):
                    self.state[affected_faces[0]][0][i], self.state[affected_faces[1]][2 - i][0], self.state[affected_faces[2]][2][2 - i], self.state[affected_faces[3]][i][2] = (
                        self.state[affected_faces[3]][i][2], self.state[affected_faces[0]][0][i], self.state[affected_faces[1]][2 - i][0], self.state[affected_faces[2]][2][2 - i]
                    )

    def scramble(self, run=10000):
        print(f">> Scramble up the cube with {run} random moves!")
        self.steps = []  # clear steps
        for _ in range(run):
            move = random.randint(0, len(Move) - 1)
            self.steps.append(move)
            self.__rotate(move)

    def restore(self):
        print(">> Restoring the cube!")
        while self.steps:
            move = self.steps.pop()
            for _ in range(3):
                self.__rotate(move)

    def test(self):
        for key, value in Move.__members__.items():
            print(f">> {key} rotate ")
            self.__rotate(value.value)
            self.show()
            for _ in range(3):
                self.__rotate(value.value)

    def solver(self):
        def cube2str(self):
            slove_state = ''
            for row in self.state["U"]:
                slove_state += ''.join(row)

            for i in range(self.length):
                slove_state += ''.join(self.state["L"][i])
                slove_state += ''.join(self.state["F"][i])
                slove_state += ''.join(self.state["R"][i])
                slove_state += ''.join(self.state["B"][i])

            for row in self.state["D"]:
                slove_state += ''.join(row)
            
            return slove_state
        
        def str2cube(self, cube_str):
            if len(cube_str) != 54:
                raise ValueError("Invalid cube string length")
            
            index = 0
            size = 3  # 3x3 Cube
            
            self.state["U"] = []
            self.state["L"] = []
            self.state["F"] = []
            self.state["R"] = []
            self.state["B"] = []
            self.state["D"] = []
            
            self.state["U"] = [list(cube_str[index + i * size : index + (i + 1) * size]) for i in range(size)]
            index += size * size

            for row in range(size):
                self.state["L"].append(list(cube_str[index : index + 3]))
                self.state["F"].append(list(cube_str[index + 3: index + 6]))
                self.state["R"].append(list(cube_str[index + 6: index + 9]))
                self.state["B"].append(list(cube_str[index + 9: index + 12]))
                index += 4 * size

            self.state["D"] = [list(cube_str[index + i * size : index + (i + 1) * size]) for i in range(size)]

        
        # call helper :D : https://github.com/pglass/cube
        scrambled_state = cube2str(self) 
        c = Cube(scrambled_state)
        solver = Solver(c)
        solver.solve()
        # print(solver.cube.flat_str())
        # print(solver.cube)
        str2cube(self, solver.cube.flat_str())


        
            


        
