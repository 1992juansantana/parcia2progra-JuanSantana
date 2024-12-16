
import pygame
import random

# Configuración inicial de Pygame
pygame.init()

# Tamaño de la pantalla
PANTALLA_TAMAÑO = (800, 600)
pantalla = pygame.display.set_mode(PANTALLA_TAMAÑO)
pygame.display.set_caption("Juego de Meteoros")

# Colores
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)

# Imágenes
nave = pygame.image.load('nave.png')
nave_impactada = pygame.image.load('nave_impactada.png')
meteoro = pygame.image.load('meteoro.png')
espacio = pygame.image.load('fondo_espacio.png')

# Variables del juego
coordenada_nave = [400, 500]
nivel = 1
velocidad_meteoro = 3
meteoritos = []
nave_actual = nave
meteoritos_esquivados = 0

# Función para generar meteoros
def generar_meteoros():
    global meteoritos
    for i in range(5):
        meteoro_rect = pygame.Rect(random.randint(0, PANTALLA_TAMAÑO[0] - 100), random.randint(-600, -100), 100, 100)
        meteoritos.append(meteoro_rect)

# Función para mostrar el menú
def mostrar_menu():
    # Aquí puedes agregar el código para el menú principal
    pass

# Función para mostrar la pantalla de Game Over
def mostrar_game_over():
    # Aquí puedes agregar el código para mostrar el mensaje de Game Over
    pass

# Función para reiniciar el juego
def reiniciar_juego():
    global meteoritos, nivel, velocidad_meteoro, meteoritos_esquivados, coordenada_nave, nave_actual
    meteoritos = []
    nivel = 1
    velocidad_meteoro = 3
    meteoritos_esquivados = 0
    coordenada_nave = [400, 500]
    nave_actual = nave
    generar_meteoros()
    juego()

# Función principal del juego
def juego():
    global meteoritos, nivel, velocidad_meteoro, tiempo_inicio, rect_nave, juego_corriendo, nave_actual, meteoritos_esquivados

    juego_corriendo = True
    rect_nave = pygame.Rect(coordenada_nave[0], coordenada_nave[1], 30, 30)
    velocidad_nave = 5

    # Generar meteoros al inicio
    generar_meteoros()

    # Variables para controlar el tiempo y el aumento de nivel
    tiempo_inicio_nivel = pygame.time.get_ticks()  # Tiempo al inicio del nivel
    tiempo_aumento_nivel = 15000  # 15 segundos (en milisegundos)

    # Bucle del juego
    while juego_corriendo:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Volver al menú
                    juego_corriendo = False
                    mostrar_menu()

        # Verificar si han pasado 15 segundos
        if pygame.time.get_ticks() - tiempo_inicio_nivel >= tiempo_aumento_nivel:
            nivel += 1  # Aumentar el nivel
            velocidad_meteoro += 1  # Aumentar la velocidad de los meteoros
            tiempo_inicio_nivel = pygame.time.get_ticks()  # Reiniciar el contador de tiempo para el siguiente nivel

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
                meteoritos_esquivados += 1  # Incrementar el contador de meteoritos esquivados

            # Detectar colisión entre la nave y el meteoro
            if rect_nave.colliderect(meteoro_rect):
                nave_actual = nave_impactada  # Cambiar la imagen de la nave al impactada
                juego_corriendo = False  # Terminar el juego si hay colisión
                break  # Salir del bucle si colisiona

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

        # Mostrar el nivel y meteoritos esquivados en la pantalla
        font = pygame.font.SysFont("Arial", 30)
        texto_nivel = font.render(f"Nivel: {nivel}", True, (255, 255, 255))
        pantalla.blit(texto_nivel, (10, 10))

        texto_esquivados = font.render(f"Esquivados: {meteoritos_esquivados}", True, (255, 255, 255))
        pantalla.blit(texto_esquivados, (PANTALLA_TAMAÑO[0] - 200, 10))

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
reiniciar_juego()
