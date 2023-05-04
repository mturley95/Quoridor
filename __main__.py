'''
Quoridor
Mitch Turley

This project will allow the user to virtually play the Quoridor game published by Gigamic games.
The user may play against another user one-on-one or against a simple bot.
This is the main codeblock to be run when the user desires to play.
'''

import os
import sys
import pygame

sys.path.append('src/')

from window import *
from const import *
from game import Game
from wall import Wall
from pathfinder import PathFinder

def play_game():
    '''Start the quoridor game.'''
    print("Welcome to Quoridor!")

    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Initialize the game.
    WIN = Window()

    # Create the font for the text
    font = pygame.font.SysFont(None, 40)

    # Set up the text input boxes
    user_input_box = pygame.Rect(100, 100, 100, 50)
    bot_input_box = pygame.Rect(300, 100, 100, 50)
    user_text = ''
    bot_text = ''

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle user input
                if event.key == pygame.K_RETURN:
                    # Get the number of users and bots
                    num_users = int(user_text)
                    num_bots = int(bot_text)
                    print("Starting game with", num_users, "users and", num_bots, "bots.")
                elif event.key == pygame.K_BACKSPACE:
                    if user_input_box.collidepoint(event.pos):
                        user_text = user_text[:-1]
                    elif bot_input_box.collidepoint(event.pos):
                        bot_text = bot_text[:-1]
                else:
                    if user_input_box.collidepoint(event.pos):
                        user_text += event.unicode
                    elif bot_input_box.collidepoint(event.pos):
                        bot_text += event.unicode

        # Draw the background and input boxes
        pygame.draw.rect(win.win, Colors.black, user_input_box, 2)
        pygame.draw.rect(win.win, Colors.black, bot_input_box, 2)

        # Draw the user input text
        user_surface = font.render(user_text, True, Colors.black)
        user_rect = user_surface.get_rect()
        user_rect.center = user_input_box.center
        win.win.blit(user_surface, user_rect)

        # Draw the bot input text
        bot_surface = font.render(bot_text, True, Colors.black)
        bot_rect = bot_surface.get_rect()
        bot_rect.center = bot_input_box.center
        win.win.blit(bot_surface, bot_rect)

        # Draw the labels for the input boxes
        user_label_surface = font.render("Number of users:", True, Colors.black)
        user_label_rect = user_label_surface.get_rect()
        user_label_rect.x = user_input_box.x - 200
        user_label_rect.centery = user_input_box.centery
        win.win.blit(user_label_surface, user_label_rect)

        bot_label_surface = font.render("Number of bots:", True, Colors.black)
        bot_label_rect = bot_label_surface.get_rect()
        bot_label_rect.x = bot_input_box.x - 200
        bot_label_rect.centery = bot_input_box.centery
        win.win.blit(bot_label_surface, bot_label_rect)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


    # Select number of players
    proper_input = False
    while proper_input == False:
        number_of_players = input("Enter the number of players (up to 4): ")
        if number_of_players.isdigit():
            player_count = int(number_of_players)
            if 1<= player_count <= 4:
                proper_input = True
            else:
                print("The input is not a valid player count. Please enter a number between 1 and 4.")

    # Name input
    name = ''
    while name == '' or len(name) > 10:
        name = input("Enter your name: ").capitalize()
        if len(name) > 10:
            print("Too long")

    player_count, num_player = int(data[0]), int(data[1])

    # Send name
    try:
        n.send(';'.join(['N', str(num_player), name]))
    except Exception:
        print("Impossible to send data to the server")
        exit()

    print("Connexion established!")
    print(f"Hello {name}! You are player {num_player}!")

    # Init pygame
    pygame.init()
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.abspath(__file__))
    # sounds = Sounds(path)

    # Init game
    win = Window()
    coords = win.coords
    players = Players(player_count, coords)
    player = players.players[num_player]
    walls = Walls()
    pf = PathFinder()

    last_play = ''
    run = True
    ready = False
    start = False

    while run:
        clock.tick(40)
        n.send('get')
        try:
            game = n.get_game()
        except Exception:
            run = False
            print("Couldn't get game")
            break

        # Start a game
        if not start:
            if not ready:
                players.set_names(game.names)
                win.update_info(
                    f"Waiting for {game.players_missing()} players...")
                ready = game.ready()
            if game.run:
                current_p = players.players[game.current_player]
                win.update_info(f"Let's go! {current_p.name} plays!",
                                current_p.color)
                try:
                    sounds.start_sound.play()
                except Exception:
                    pass
                start = True
            elif game.wanted_restart != []:
                nb = len(game.wanted_restart)
                p = players.players[game.wanted_restart[-1]]
                win.update_info(
                    f"{p.name} wants to restart! ({nb}/{player_count})",
                    p.color)

        # Continue a game
        else:
            get_play = game.last_play
            if get_play != '' and get_play != last_play:
                if get_play[0] == 'D':
                    current_p = players.players[game.current_player]
                    win.update_info(f"{current_p.name} plays!",
                                    current_p.color)
                elif get_play[0] == 'P':
                    if players.play(get_play, coords, walls, pf):
                        current_p = players.players[game.current_player]
                        win.update_info(f"{current_p.name} plays!",
                                        current_p.color)
                    else:
                        win.update_info(f"{game.winner} wins!")
                        try:
                            sounds.winning_sound.play()
                        except Exception:
                            pass
                        win.button_restart.show = True
                        start = False
                last_play = get_play

        pos = pygame.mouse.get_pos()
        win.redraw_window(game, players, walls, pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if win.button_quit.click(pos):
                    run = False
                    pygame.quit()
                elif (not game.run and win.button_restart.click(pos)
                        and win.button_restart.show):   # Restart
                    coords.reset()
                    players.reset(coords)
                    walls.reset()
                    pf.reset()
                    win.button_restart.show = False
                    n.send(';'.join(['R', str(num_player)]))
                elif player.can_play_wall(game):    # Put a wall
                    mes = player.play_put_wall(
                        pos, coords, walls, n, pf, players)
                    if mes != '':
                        win.update_info(mes)

            elif event.type == pygame.KEYDOWN:  # Move pawn
                if player.can_play(game):
                    player.play_move(walls, n)

    print("Good bye!")


if __name__ == "__main__":
    pygame.init()
    WIN = Window()
    # play_game()