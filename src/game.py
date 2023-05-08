from src.player import Players

class Game:
    '''
    Create a game.

    Add more info about the game class here.
    '''

    def __init__(self, player_count):
        '''
        Initialize the game class.
        
        Add more info about this function's parameters here.
        '''

        self.player_count = player_count
        # A list of all of the players.
        self.players = []
        # The game is not running until it is started.
        self.running = False
        # Used to find the current player by taking the last value of a list.
        self.current_player = -1
        self.last_play = ''
        self.winner = ''
        

    def set_player_count(self, new_player_count):
        self.player_count = new_player_count


    def next_player(self, current):
        '''
        Return the new current player.

        Add more info about this function's parameters here.
        '''
        
        # Add one to the player who just played and 
        # take its modulus from the player count to find who plays next. 
        current = (current + 1) % self.player_count
        return current
    

    def get_name_current(self, players):
        '''
        Return the name of the current player.
        
        Add more info about this function's parameters here.
        '''

        # Return the name of the current player.
        return players.players[self.current_player].name
    

    def start(self):
        '''
        Start the game.
        
        Add more info about this function's parameters here.
        '''

        self.winner = ''
        # Start with player_0 ("Player 1")
        self.current_player = self.next_player(-1)
        # Run the game.
        self.running = True
        print("Quoridor game started!")


    def play(self, players):
        '''
        Get a move.
        
        Add more info about this function's parameters here.
        '''

        # If the player wins,
        if players.players[self.current_player].has_win\
            (players.players[self.current_player].coord) == True:
            # Print the winner's name.
            self.winner = self.get_name_current(players)
            print(f"{self.winner} wins!")
            self.current_player = -1
            # Stop running the program.
            self.running = False
            running = False
            end = True
            return running, end

        # If not a winning play, 
        else:
            # Go to the next player.
            running = True
            end = False
            self.current_player = self.next_player(self.current_player)
            return running, end
