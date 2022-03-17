#NAMBI RAMANAN
#FROM BABHA BATCH
import fileinput

class Maze_Solver:
    def solve_Maze(self, mat): #Creating a matrix with 0 to reach the target
        result_mat = [[0 for i in range(x_coordinate)]for j in range(y_coordinate)]
        if res.way_Maze(mat, 0, 0, result_mat) is False:
            return False
        res.Remove_Path(result_mat)
        return result_mat

    def way_Maze(self, mat, row_index, column_index, result_mat):
        # base case check if the pointers reached the end point
        if mat[y_coordinate - 1][x_coordinate - 1] == 1 and result_mat[y_coordinate - 1][x_coordinate - 1] == 1:
            return True

        # checks if it is safe to move to the pointers location by calling another method
        if res.valid(mat, row_index, column_index, result_mat) is True:
            result_mat[row_index][column_index] = 1
            Maze_Solver.pointer_Mover(self, mat, row_index, column_index, result_mat)
        else:
            return False

        if result_mat[y_coordinate - 1][x_coordinate - 1] == 0:
            return False

    #Check the coordinates while you moving the pointers
    def valid(self, mat, row_pointer, column_pointer, result_mat):
        if row_pointer < y_coordinate and column_pointer < x_coordinate and mat[row_pointer][column_pointer] == 1:
            return True
        return False
        
    def pointer_Mover(self, mat, row_pointer, column_pointer, result_mat):
        # moving pointer rightward will be valid or not
        if res.way_Maze(mat, row_pointer, column_pointer + 1, result_mat) is True:
            return True
        # moving pointer leftward will be valid or not
        elif result_mat[row_pointer][column_pointer - 1] == 0 and mat[row_pointer][column_pointer - 1] == 1 and column_pointer != 0:
            res.way_Maze(mat, row_pointer, column_pointer - 1, result_mat)
            return True
        # moving pointer downward will be valid or not
        if res.way_Maze(mat, row_pointer + 1, column_pointer, result_mat) is True:
            return True
        # moving pointer upward will be valid or not
        elif result_mat[row_pointer - 1][column_pointer] == 0 and mat[row_pointer - 1][column_pointer] == 1 and row_pointer != 0:
            res.way_Maze(mat, row_pointer - 1, column_pointer, result_mat)
            return True
        return False

    #Checking visited paths
    def Remove_Path(self, result_mat):
        for _ in range(0, x_coordinate):
            for i in range(1, len(result_mat) - 1):
                for j in range(1, len(result_mat[0]) - 1):
                    if result_mat[i][j] == 1:
                        # checks every element in the result Matrix with three directions blocked
                        if result_mat[i + 1][j] == 0 and result_mat[i - 1][j] == 0 and result_mat[i][j + 1] == 0:
                            result_mat[i][j] = 0
                        if result_mat[i + 1][j] == 0 and result_mat[i - 1][j] == 0 and result_mat[i][j - 1] == 0:
                            result_mat[i][j] = 0
                        if result_mat[i - 1][j] == 0 and result_mat[i][j + 1] == 0 and result_mat[i][j - 1] == 0:
                            result_mat[i][j] = 0
                        if result_mat[i + 1][j] == 0 and result_mat[i][j + 1] == 0 and result_mat[i][j - 1] == 0:
                            result_mat[i][j] = 0
        return True


#input from input (text file)
mat = []
Input = str(input("Enter the name of Input file:-"))
for line in fileinput.input(files=(Input)):
    element = list(map(int, line.split()))
    mat.append(element)

#Coordinates of matrix
x_coordinate = len(mat[0])
y_coordinate = len(mat)

#Assign class
res = Maze_Solver()