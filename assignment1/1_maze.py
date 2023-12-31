
def create_maze():
    maze = {
        # defining the maze
        # (COLUMN, ROW)
        # following what mr yessen made in class
        (0, 0): [(0, 1)],
        (0, 1): [(0, 2)],
        (0, 2): [(0, 3)],
        (0, 3): [(0, 4), (1, 3)],
        (1, 3): [(1, 2), (1, 4), (2, 3)],
        (2, 3): [],
        (1, 2): [(1, 1)],
        (1, 1): [(1, 0)],
        (1, 0): [(2, 0)],
        (2, 0): [(3, 0)],
        (3, 0): [(3, 1)],
        (3, 1): [(2, 1), (3, 2)],
        (2, 1): [],
        (3, 2): [(2, 2), (4, 2)],
        (2, 2): [],
        (4, 2): [(4, 1)],
        (0, 4): [],
        (1, 4): [(2, 4)],
        (2, 4): [(3, 4)],
        (3, 4): [(4, 4)],
        (4, 4): [(4, 3)],
        (4, 3): [(3, 3)],
        (3, 3): []
    }
    return maze

def bfs(maze, start, end):
    visited = []
    bfs_q = []
    bfs_q.append(start)

    while bfs_q:
        z = bfs_q.pop(0)
        visited.append(z)
        if len(visited) == 1:
            print("visit:", z, "(S)")
        else:
            print("visit:", z)

        if z == end:
            print("\n")
            print("end of the point:", end, "(G)")
            break

        for i in maze[z]:
            if i not in visited and i not in bfs_q:
                bfs_q.append(i)
                print("the neighbour added:", i)

# run BFS
def main():
    while True:
        print("1. Use default starting point (0.0) and ending point (2,1) ")
        print("2. Manually enter between (0,0) to (4,4)")
        a = input("Please choose between 1 and 2: ")

        if a == '1':
            start = (0, 0)
            target = (2, 1)
            break
        elif a == '2':
            start = eval(input("Please enter your point of start (0,0 to 4,4) as (column, row): "))
            target = eval(input("Please enter your point of end (0,0 to 4,4) as (column, row): "))
            if 0 <= start[0] <= 5 and 0 <= start[1] <= 5 and 0 <= target[0] <= 5 and 0 <= target[1] <= 5:
                break
            else:
                print("Invalid input. Row and column values must be between 0 and 5.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    maze = create_maze()
    bfs(maze, start, target)

while True:
    main()
    print("\n")
    try_again = input("Do you want to try again? (y): ")
    if try_again.lower() == "y":
        continue
    else:
        print("Thank you!")
        break


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

#     print("Current bfs_q:", Q)

# print("Visited cells:", visited)
