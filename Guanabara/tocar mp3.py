import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Gintama Opening 13.mp3')
pygame.mixer.music.play(loops=8, start=70.0, fade_ms= 0)
pygame.event.wait()