import pygame
from constantes import *
from funciones import mostrar_menu





# Inicialización
pygame.init()
pygame.mixer.init()  # Iniciar el sistema de música de pygame

pantalla = pygame.display.set_mode(PANTALLA_TAMAÑO)

# Cargar imágenes

nave = pygame.image.load("./practicando_clases/TATETI/nave.png")
nave = pygame.transform.scale(nave, (100, 100))
    
nave_impactada = pygame.image.load("./practicando_clases/TATETI/nave_impactada.png")
nave_impactada = pygame.transform.scale(nave_impactada, (100, 100))



meteoro = pygame.image.load("./practicando_clases/TATETI/meteoro.png")
meteoro = pygame.transform.scale(meteoro, (100, 100))



espacio = pygame.image.load("./practicando_clases/TATETI/espacio.png")
espacio = pygame.transform.scale(espacio, (800, 600))


# Cargar música

pygame.mixer.music.load('./practicando_clases/TATETI/musica.mp3')  
pygame.mixer.music.set_volume(0.5)  

# nombre de la ventana
pygame.display.set_caption("JUEGO UTN")

puntuacion = 0


mostrar_menu(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)





# Salir del juego
pygame.quit()


