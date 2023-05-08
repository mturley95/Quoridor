class Game:
    '''
    This class starts and manages the game.
    
    Values:
        * player_count (int)
        * players (list)
        * running (bool)
        * current_player_number (int)
        * winner (str)

    Functions:
        * __init__(self, player_count)
        * set_player_count(self, new_player_count)
        * next_player(self, current)
        * get_name_current(self, players)
        * start(self)
        * play(self, players)
    '''

    def __init__(self, player_count):
        '''
        This function initializes the Game class.

        **Parameters**
            player_count: *int*
                The integer value of the current number of players.

        **Returns**
            N/A
        '''

        self.player_count = player_count
        # A list of all of the players.
        self.players = []
        # The game is not running until it is started.
        self.running = False
        # Used to find the current player by taking the last value of a list.
        self.current_player_number = -1
        # Set a winner variable to be updated when a player wins the game.
        self.winner = ''
        

    def set_player_count(self, new_player_count):
        '''
        This function updates the game's player count to a new value that is provided.

        **Parameters**
            new_player_count: *int*
                New player count for players in the game.

        **Returns**
            N/A
        '''

        # Change the game's player count to a new player count that is provided.
        self.player_count = new_player_count


    def next_player(self, current_player_number):
        '''
        This function updates the game's current player to the next player and
        returns the new current player number.

        **Parameters**
            current_player_number: *int*
                The integer value of the current player that is playing.

        **Returns**
            current_player_number: *int*
                The integer value of the updated current player that is playing.
        '''
        
        # Add one to the player who just played and 
        # take its modulus from the player count to find who plays next. 
        current_player_number = (current_player_number + 1) % self.player_count
        return current_player_number
    

    def get_name_current(self, players):
        '''
        This function returns the name of the current player.

        **Parameters**
            players: *int*
                New player count for players in the game.

        **Returns**
            current_player_name: *str*
                The name of the current player.
        '''

        # Return the name of the current player.
        return players.players[self.current_player_number].name
    

    def start(self):
        '''
        This function starts the game.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Set the winner variable blank.
        self.winner = ''
        # Start with player_0 ("Player 1").
        self.current_player_number = self.next_player(-1)
        # Run the game.
        self.running = True
        print("Quoridor game started!")


    def play(self, players):
        '''
        This function gets and plays a move.
        It checks to see if the player that moved has won before
        continuing to the next player.
        
        **Parameters**
            players: *Players obj*
                This is a Players object that contains a list of all of the players.

        **Returns**
            running: *bool*
                The game keeps running if the player did not win (running = True).
            end: *bool*
                The game ends if the player did win (end = True).
        '''

        # If the player wins,
        if players.players[self.current_player_number].has_win\
            (players.players[self.current_player_number].coord) == True:
            # Print the winner's name.
            self.winner = self.get_name_current(players)
            print(f"{self.winner} wins!")
            self.current_player_number = -1
            # Stop running the game loop but keep the window open.
            self.running = False
            running = False
            end = True
            # Return the status that the game has ended.
            return running, end

        # If not a winning play, 
        else:
            # Go to the next player.
            running = True
            end = False
            self.current_player_number = self.next_player(self.current_player_number)
            # Return the status that the game keeps running.
            return running, end
