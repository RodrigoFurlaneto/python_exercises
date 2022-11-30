# This program will play music
import pygame
pygame.mixer.init()
pygame.init()
# Replace the '**' with the name of the mp3 file
pygame.mixer.music.load('***')
pygame.mixer.music.play()
pygame.event.wait()
