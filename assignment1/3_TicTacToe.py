import math
import copy

class TicTacToe:
    def __init__(self, state=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.state = state

    def make_move(self, row, col, val):
        if 0 <= row < 3 and 0 <= col < 3 and self.state[row][col] == 0:
            self.state[row][col] = val
            return True
        return False

    def terminal_node(self, state):
        result = 0
        is_game_over = False

        empty_cells = False
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_cells = True

        # Check rows and columns
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] != 0 or state[0][i] == state[1][i] == state[2][i] != 0:
                is_game_over = True
                result = state[i][0] * 10

        # Check diagonals
        if state[0][0] == state[1][1] == state[2][2] != 0 or state[0][2] == state[1][1] == state[2][0] != 0:
            is_game_over = True
            result = state[1][1] * 10

        is_game_over = is_game_over or not empty_cells
        return {"game_over": is_game_over, "result": result}

    def expand_state(self, state):
        children = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    child = [i, j]
                    children.append(child)
        return children

    def evaluate_state(self, state):
        x_count = sum(row.count(1) for row in state)  # num x
        o_count = sum(row.count(-1) for row in state)  # num o
        return x_count - o_count  # diff of x n o


    def modified_maximax(self, state, depth, is_max_player):
        if depth == 0 or self.terminal_node(state)["game_over"]:
            return self.evaluate_state(state)

        if is_max_player:
            top_worth = -math.inf
            children = self.expand_state(state)
            for pos in children:
                child = copy.deepcopy(state)
                child[pos[0]][pos[1]] = 1
                v = self.modified_maximax(child, depth - 1, not is_max_player)
                top_worth = max(top_worth, v)
            return top_worth
        else:
            top_worth = math.inf
            children = self.expand_state(state)
            for pos in children:
                child = copy.deepcopy(state)
                child[pos[0]][pos[1]] = -1
                v = self.modified_maximax(child, depth - 1, not is_max_player)
                top_worth = min(top_worth, v)
            return top_worth

    def computer_move(self):
        is_max_player = True
        optimum_movement = None
        top_worth = -math.inf
        depth = 9 

        for move in self.expand_state(self.state):
            child = copy.deepcopy(self.state)
            child[move[0]][move[1]] = 1  # Simulate a computer move
            worth = self.modified_maximax(child, depth - 1, not is_max_player)

            if worth > top_worth:
                top_worth = worth
                optimum_movement = move

        if optimum_movement is not None:
            row, col = optimum_movement
            self.make_move(row, col, 1)  # Make the best computer move

    def generate_CLI(self):
        print("\t" + "-------------")
        for i in range(3):
            print("\t" + "|", end=" ")
            for j in range(3):
                if self.state[i][j] == -1:
                    print("X", end=" | ")
                elif self.state[i][j] == 1:
                    print("O", end=" | ")
                else:
                    print("#", end=" | ")
            print("\n\t" + "-------------")



    def start(self):
        game_start = True
        round = 0
        a = 0  
        while a == 0: 
            round = round + 1
            print("\n")
            print("\t" + "Round " + str(round).center(20))
            self.generate_CLI()
            col = int(input("\tColumn (1-3): "))
            row = int(input("\tRow (1-3):"))
            col = col - 1
            row = row - 1
            
            if self.make_move(row, col, -1):
                if self.terminal_node(self.state)["game_over"]:
                    self.generate_CLI()
                    result = self.terminal_node(self.state)["result"]
                    if result == -10:
                        print("\tYou win!")
                    elif result == 10:
                        print("\tYou lose!")
                    else:
                        print("\tIt's a draw!")
                    break
                self.computer_move()
                if self.terminal_node(self.state)["game_over"]:
                    self.generate_CLI()
                    result = self.terminal_node(self.state)["result"]
                    if result == -10:
                        print("\tYou win!")
                    elif result == 10:
                        print("\tYou lose!")
                    else:
                        print("\tIt's a draw!")
                    break


play = TicTacToe()
play.start()
