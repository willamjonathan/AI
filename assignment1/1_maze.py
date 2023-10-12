
def create_maze():
    maze = {
        #defining the maze
        #(COLUMN,ROW)
        #following what mr yessen made in class
        "0,0": ["0,1"],
        "0,1":["0,2"],
        "0,2":["0,3"],
        "0,3":["0,4","1,3"],
        "1,3":["1,2","1,4","2,3"],
        "2,3":[],
        "1,2":["1,1"],
        "1,1":["1,0"],
        "1,0":["2,0"],
        "2,0":["3,0"],
        "3,0":["3,1"],
        "3,1":["2,1","3,2"],
        "2,1":[],
        "3,2":["2,2","4,2"],
        "2,2":[],
        "4,2":["4,1"],
        "0,4":[],
        "1,4":["2,4"],
        "2,4":["3,4"],
        "3,4":["4,4"],
        "4,4":["4,3"],
        "4,3":["3,3"],
        "3,3":[]        
    }
    return maze

def bfs(maze, start, end):
    visited = []
    queue = []
    queue.append(start)

    while queue:
        u = queue.pop(0)
        visited.append(u)
        print("visited:", u)

        if u == end:
            print("end of the point:", end, "(G)")
            break

        for v in maze[u]:
            if v not in visited and v not in queue:
                queue.append(v)
                print("added neighbour:", v)

# run BFS
def main():
    start = "0,0"
    target = "2,1"
    maze = create_maze()
    bfs(maze, start, target)

main()


#I actually have tried to make a different version of the maze, not following the one in class
#but sadly it doesnt work as how i wished it work..

# def create_maze():
#     maze = [
#         # top, left, bottom, right
#         # 0 = no wall, 1 = wall, 2 = path
#         [[1, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 0, 1]],  # row 1
#         [[0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1]],  # row 2
#         [[0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]],  # row 3
#         [[0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 1, 1, 0], [0, 0, 0, 1]],  # row 4
#         [[0, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1]],  # row 5
#     ]
#     return maze
# def is_valid_move(row, col, maze, visited):
#     # 5 is the number of row and column
#     if 0 <= row < 5:
#         if 0 <= col < 5:
#             if (row, col) not in visited: #have to be not visited to avoid revisiting cells that have been visited
#                 for i in range (4):
#                     if maze[row][col][i]==0:
#                         return True
#                     else:
#                         return False
#     return False
# maze = create_maze()
# r_start, c_start = 0, 0
# r_end, c_end = 1, 2
# end = (r_end, c_end)
# visited = set()
# Q = [(r_start, c_start)]  

# while Q:
#     u = Q.pop(0)
#     visited.add(u)

#     if u == end:
#         print("Reached the target (row, column): " + str(end))
#         break

#     row, col = u

#     #direction of movement
#     moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # top,left,bottom, down
#     for move in moves:
#         new_row, new_col = row + move[0], col + move[1]
#         if is_valid_move(new_row, new_col, maze, visited):
#             Q.append((new_row, new_col)) #appending to the Q
#             visited.add((new_row, new_col))  # input to visited

#     print("Current Queue:", Q)

# print("Visited cells:", visited)
