from cube import RubikCube

if __name__ == '__main__':
    myCube = RubikCube()
    myCube.show()
    myCube.scramble(run = 1000000)
    myCube.show()
    myCube.solver()
    myCube.show()