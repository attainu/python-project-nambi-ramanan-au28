import argparse
import main as Maze_solver


def Main():
    pars = argparse.ArgumentParser()
    pars.add_argument("-o", "--outputfile", help="Output the result to a file", action="store_true")
    pars.add_argument("-i", "--inputfile", help="Output the result to a file", action="store_true")
    ars = pars.parse_args()
    if ars.outputfile:
        data = open("outputfile.txt", "a")
        if Maze_solver.res.solve_Maze(Maze_solver.mat) is False:
            data.write(str("-1"))
        else:
            for i in Maze_solver.res.solve_Maze (Maze_solver.mat):
                for result in i:
                    data.write(str(result) + " ")
                data.write('\n')


Maze_solver.res.solve_Maze(Maze_solver.mat)

if __name__ == '__main__':
    Main()