class Game:
    board = [[' ' for j in range(3)] for i in range(3)]   
    turn = 'X'

    def __init__(self):
        pass


    def game_over(self):   # x wins => 'X', 0 wins => '0', tie => 't', not over => 'n'
        # check lines
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return self.board[i][0]
            
        # check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != ' ':
                return self.board[0][j]
            
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        
        # check for a tie
        ok = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    ok = 1
        if ok == 0:
            return 't'

        return 'n'
    

    def utility(self):
        if self.game_over() == 'X':
            return 1
        if self.game_over() == '0':
            return -1
        if self.game_over() == 't':
            return 0


    def winner(self, a):
        if a == 'X':
            print("X has won")
        if a == '0':
            print("0 has won")
        if a == 't':
            print("Tie")


    def minimax(self, turn):
        if self.game_over() != 'n':
            return self.utility()
        
        if turn == 'X':
            best_value = -100
            # consider all possible moves
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        #self.display_board()
                        value = self.minimax('0')
                        self.board[i][j] = ' '
                        if value > best_value:
                            best_value = value
        else:
            best_value = 100
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = '0'
                        #self.display_board()
                        value = self.minimax('X')
                        self.board[i][j] = ' '
                        if value < best_value:
                            best_value = value      
        return best_value


    def play(self):
        while self.game_over() == 'n':
            # check whose turn it is
            if self.turn == 'X':
                best_value = -100
                # x and y optimal coordinates
                x = -1
                y = -1
                # consider all possible moves
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            self.board[i][j] = 'X'
                            value = self.minimax('0')
                            print(value)
                            self.board[i][j] = ' '
                            if value > best_value:
                                best_value = value
                                x = i
                                y = j
                self.board[x][y] = 'X'
                self.display_board()
                self.turn = '0'
            else:
                ok = False
                while ok == False:
                    move = input("Enter the coordinates of your move: ")
                    x = int(move[0])
                    y = int(move[2])
                    ok = self.valid_move(x, y)
                self.board[x][y] = '0'
                self.turn = 'X'
                self.display_board()

        self.winner(self.game_over())


    def valid_move(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Invalid move")
            return False
        if self.board[x][y] != ' ':
            print("Invalid move")
            return False
        return True


    def display_board(self):
        print("  0 1 2")
        for i in range(3):
            print(i, ' '.join(self.board[i]))
        print('')


game = Game()
game.play()
