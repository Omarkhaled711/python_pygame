#!/usr/bin/env python3

import characters.bullet as bullet
import characters.enemy as enemy
import characters.player as player
import os
import pygame
import random
import settings.audio as audio
import settings.gui as gui
import TextRendering.text as text

if __name__ == '__main__':
    pygame.init()

    # Set up paths for images and sound files
    images_path = os.getcwd() + '/images/'
    sound_path = os.getcwd() + '/sound/'

    # Initialize window settings
    gui = gui.Window(
        height=600, width=800, title='Space Invaders',
        logo_path=images_path+'logo.png',
        background_path=images_path+'background.png')

    # Initialize player settings
    spaceCraft = player.Player(
        x=370, y=480, image_path=images_path + 'player.png', speed=8)

    # Initialize enemy settings
    enemy_x_min = 0
    enemy_x_max = gui.width
    enemy_y_min = 50
    enemy_y_max = 0.2 * gui.height
    enemy_count_text = text.Text(text="Enemies", size=32,
                                 x=gui.width - 200, y=10)
    enemy_count = 0
    enemies_max = 10
    enemy_list = []

    # Initialize bullet settings
    bullet_y = spaceCraft.y + 10
    bullet = bullet.Bullet(
        x=0, y=bullet_y, image_path=images_path + 'bullet.png',
        sound_file=sound_path+'bullet.mp3')

    # Initialize score settings
    score_text = text.Text(text="Score", size=32, x=10, y=10)
    score = 0
    bullet_centring_factor = 16

    # Play background music
    audio.Music(sound_file=sound_path+'background.mp3', loop_state=1)

    # Game loop variables
    running = True
    gameover_state = 0
    start_play = 1

    while running:
        gui.screen.fill((0, 0, 0))  # Clear the screen
        gui.draw_background()

        # Display game over screen if the game is over
        if gameover_state == 1:
            gameover = text.Text(
                text="Game Over", size=64, x=gui.width/2 - 170, y=gui.height/2 - 50)
            gameover.show_text(gui.screen)
            playagain_text = text.Text(
                "Press Space to play again", size=24, x=gui.width/2 - 150, y=gui.height/2 + 40)
            playagain_text.show_text(gui.screen)

        # Create the first enemy when the game starts
        elif start_play == 1:
            enemy_list.append(enemy.Enemy(x=random.randint(enemy_x_min, enemy_x_max),
                                          y=random.randint(
                                              enemy_y_min, enemy_y_max),
                                          image_path=images_path + 'enemy.png', speed=3))
            enemy_count += 1
            start_play = 0
            score = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if gameover_state == 1 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover_state = 0
                    start_play = 1

            # Handle player movement
            spaceCraft.move(event)
            # Handle bullet movement
            bullet.move(event)

        spaceCraft.draw(gui)  # Draw the player

        for curr_enemy in enemy_list:
            curr_enemy.draw(gui)

        bullet.x = spaceCraft.x + bullet_centring_factor  # Center the bullet
        bullet.draw(gui)

        score_text.show_text(gui.screen, score)  # Display the score
        enemy_count_text.show_text(
            gui.screen, enemy_count)  # Display enemy count

        for curr_enemy in enemy_list:
            # Check for collision between player and enemy
            if spaceCraft.did_Collide(curr_enemy.x, curr_enemy.y):
                gameover_state = 1
                enemy_list.clear()
                enemy_count = 0
                break

            # Check for collision between bullet and enemy
            if bullet.did_Collide(curr_enemy.x, curr_enemy.y):
                score += 1
                curr_enemy.x = random.randint(enemy_x_min, enemy_x_max)
                curr_enemy.y = random.randint(enemy_y_min, enemy_y_max)
                if len(enemy_list) < enemies_max:
                    new_enemy = enemy.Enemy(x=random.randint(enemy_x_min, enemy_x_max),
                                            y=random.randint(
                        enemy_y_min, enemy_y_max),
                        image_path=images_path + 'enemy.png', speed=3)
                    enemy_list.append(new_enemy)
                    enemy_count += 1
        pygame.display.update()
