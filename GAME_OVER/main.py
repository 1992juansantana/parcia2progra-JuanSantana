import pygame
import random
from constantes import *

# Inicialización
pygame.init()
pygame.mixer.init()  # Iniciar el sistema de música de pygame

# Constantes
PANTALLA_TAMAÑO = (800, 600)
COLOR_NEGRO = (0, 0, 0)
COLOR_CELESTE = (0, 0, 128)
coordenada_nave = [300, 500]  # Posición inicial de la nave
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

# Función para reiniciar el juego
def reiniciar_juego():
    global meteoritos, rect_nave, nivel, velocidad_meteoro, tiempo_inicio, nave_actual
    # Reiniciar la nave y la lista de meteoros
    rect_nave = pygame.Rect(coordenada_nave[0], coordenada_nave[1], 30, 30)                                       
    meteoritos = []
    generar_meteoros()  # Regenerar meteoros
    nivel = 1
    velocidad_meteoro = 3
    tiempo_inicio = pygame.time.get_ticks()  # Resetear el tiempo
    nave_actual = nave  # Restablecer la imagen de la nave
    return True

# Generar meteoros aleatorios
def generar_meteoros():
    for _ in range(5):  # Crear 5 meteoros al principio
        x = random.randint(0, PANTALLA_TAMAÑO[0] - 100)  # Posición aleatoria en el eje X
        y = random.randint(-600, -100)  # Posición aleatoria fuera de la pantalla en el eje Y
        meteoro_rect = pygame.Rect(x, y, 50, 50)
        meteoritos.append(meteoro_rect)

# Función para mostrar el mensaje de Game Over y opciones de reiniciar o salir
def mostrar_game_over():
    font_game_over = pygame.font.SysFont("Arial", 60)
    mensaje_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
    pantalla.blit(mensaje_game_over, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 3))

    font_reintentar = pygame.font.SysFont("Arial", 40)
    mensaje_reintentar = font_reintentar.render("Presiona R para reintentar o Q para salir", True, (255, 255, 255))
    pantalla.blit(mensaje_reintentar, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2))

    pygame.display.flip()  # Actualizar la pantalla

# Bucle principal del juego
def juego():
    global meteoritos, nivel, velocidad_meteoro, tiempo_inicio, rect_nave, juego_corriendo, nave_actual

    juego_corriendo = True
    rect_nave = pygame.Rect(coordenada_nave[0], coordenada_nave[1], 30, 30)
    velocidad_nave = 5
    velocidad_meteoro = 3
    meteoritos = []
    nave_actual = nave

    # Generar meteoros al inicio
    generar_meteoros()

    # tiempos de meteoritos
    tiempo_inicio = pygame.time.get_ticks()  # Tiempo al inicio del juego
    nivel = 1
    contador_meteoros = 0  # Para contar meteoros caídos

    # Reproducir música
    pygame.mixer.music.play(-1)

    # Bucle principal del juego
    while juego_corriendo:
       
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False

        # Movimiento de la nave
        lista_teclas_presionadas = pygame.key.get_pressed()
        if lista_teclas_presionadas:
            if lista_teclas_presionadas[pygame.K_LEFT]: 
                rect_nave.x -= velocidad_nave  # Mover a la izquierda
                if rect_nave.left < 0:  # Si se sale por el lado izquierdo
                    rect_nave.left = 0  # Ajustar al borde izquierdo de la pantalla
                
            if lista_teclas_presionadas[pygame.K_RIGHT]: 
                rect_nave.x += velocidad_nave  # Mover a la derecha
                if rect_nave.right > PANTALLA_TAMAÑO[0]:  # Si se sale por el lado derecho
                    rect_nave.right = PANTALLA_TAMAÑO[0]  # Ajustar al borde derecho de la pantalla
           
            if lista_teclas_presionadas[pygame.K_UP]: 
                rect_nave.y -= velocidad_nave  # Mover hacia arriba
                if rect_nave.top < 0:  # Si se sale por el lado superior
                    rect_nave.top = 0  # Ajustar al borde superior de la pantalla
           
            if lista_teclas_presionadas[pygame.K_DOWN]: 
                rect_nave.y += velocidad_nave  # Mover hacia abajo
                if rect_nave.bottom > PANTALLA_TAMAÑO[1]:  # Si se sale por el lado inferior
                    rect_nave.bottom = PANTALLA_TAMAÑO[1]  # Ajustar al borde inferior de la pantalla

        # Mover los meteoros
        for meteoro_rect in meteoritos:
            meteoro_rect.y += velocidad_meteoro  # Mover meteoro hacia abajo
            if meteoro_rect.top > PANTALLA_TAMAÑO[1]:  # Si el meteoro se sale por la parte inferior
                meteoro_rect.y = random.randint(-600, -100)  # Reposicionar el meteoro en la parte superior
                meteoro_rect.x = random.randint(0, PANTALLA_TAMAÑO[0] - 100)  # Reposicionar en una nueva posición X aleatoria
                contador_meteoros += 1  # Contar el meteoro que cayó

            # Detectar colisión entre la nave y el meteoro
            if rect_nave.colliderect(meteoro_rect):
                nave_actual = nave_impactada  # Cambiar la imagen de la nave al impactada
                juego_corriendo = False  # Terminar el juego si hay colisión
                break  # Salir del bucle si colisiona

        # Control de tiempo y subir de nivel cada 15 segundos
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual
        if (tiempo_actual - tiempo_inicio) >= 15000:  # Si han pasado 15 segundos (15000 ms)
            nivel += 1  # Subir de nivel
            velocidad_meteoro += 1  # Aumentar la velocidad de los meteoros
            tiempo_inicio = tiempo_actual  # Resetear el tiempo de inicio
            generar_meteoros()  # Generar más meteoros cuando sube de nivel

        # Dibujar fondo y objetos
        pantalla.fill(COLOR_NEGRO)  # Llenar la pantalla de negro antes de dibujar
        if espacio:
            pantalla.blit(espacio, [0, 0])  # Dibujar fondo de espacio

        # Dibujar meteoros
        for meteoro_rect in meteoritos:
            if meteoro:
                pantalla.blit(meteoro, meteoro_rect.topleft) 

        # Dibujar la nave con la imagen actual (normal o impactada)
        if nave_actual:
            pantalla.blit(nave_actual, rect_nave.topleft)  

        # Mostrar el nivel en la pantalla
        font = pygame.font.SysFont("Arial", 30)
        texto_nivel = font.render(f"Nivel: {nivel}", True, (255, 255, 255))
        pantalla.blit(texto_nivel, (10, 10))

        # Actualizar la pantalla
        pygame.display.flip()

    # Mostrar mensaje de Game Over
    mostrar_game_over()

    # Detener la música cuando el juego termine
    pygame.mixer.music.stop()

    # Esperar la respuesta del jugador para reintentar o salir
    esperando_reinicio = True
    while esperando_reinicio:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                esperando_reinicio = False
                juego_corriendo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:  # Si presiona "R" reintenta el juego
                    reiniciar_juego()
                    esperando_reinicio = False
                elif evento.key == pygame.K_q:  # Si presiona "Q" sale del juego
                    esperando_reinicio = False
                    juego_corriendo = False

# Iniciar el juego
juego()

# Salir del juego
pygame.quit()
