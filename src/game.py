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
        

    def add_players(self, player_count):
        '''
        Add a player.
        
        Add more info about this function's parameters here.
        '''

        # For the number of players in the game,
        for num_player in range(player_count):
            # Assign their names to be "Player X" (ex: "Player 1").
            self.players.append(f"Player {num_player+1}")


    def next_player(self, current):
        '''
        Return the new current player.

        Add more info about this function's parameters here.
        '''
        
        # Add one to the player who just played and 
        # take its modulus from the player count to find who plays next. 
        current = (current + 1) % self.player_count
        return current
    

    def get_name_current(self):
        '''
        Return the name of the current player.
        
        Add more info about this function's parameters here.
        '''

        # Return the name of the current player.
        return self.players[self.current_player]
    

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


    def play(self):
        '''
        Get a move.
        
        Add more info about this function's parameters here.
        '''

        # If the player wins,
        if player.has_win() == True:
            # Print the winner's name.
            print(f"{self.get_name_current()} wins!")
            self.winner = self.get_name_current()
            self.current_player = -1
            # Stop running the program.
            self.running = False

        # If not a winning play, 
        else:
            # Go to the next player.
            self.current_player = self.next_player(self.current_player)
