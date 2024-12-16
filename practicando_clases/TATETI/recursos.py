import pygame

def cargar_imagen(ruta, tamaño=None):
    try:
        imagen = pygame.image.load(ruta)
        if tamaño:
            imagen = pygame.transform.scale(imagen, tamaño)
        return imagen
    except pygame.error as e:
        print(f"Error al cargar la imagen {ruta}: {e}")
        pygame.quit()
        exit()

def cargar_musica(ruta):
    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Error al cargar la música {ruta}: {e}")
        pygame.quit()
        exit()

# recursos.py


