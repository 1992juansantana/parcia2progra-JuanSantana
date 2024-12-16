import pygame
import random
from constantes import *


def reiniciar_juego(nave, meteoritos, rect_nave, nivel, velocidad_meteoro, tiempo_inicio, nave_actual):
    # global meteoritos, rect_nave, nivel, velocidad_meteoro, tiempo_inicio, nave_actual
    # Reiniciar la nave y la lista de meteoros
    rect_nave = pygame.Rect(coordenada_nave[0], coordenada_nave[1], 30, 30)                                       
    meteoritos = []
    generar_meteoros()  # Regenerar meteoros
    nivel = 1
    velocidad_meteoro = 3
    tiempo_inicio = pygame.time.get_ticks()  # Resetear el tiempo
    nave_actual = nave  # Restablecer la imagen de la nave
    return meteoritos, rect_nave, nivel, velocidad_meteoro, tiempo_inicio, nave_actual


# Generar meteoros aleatorios
def generar_meteoros():
    for _ in range(5):  # Crear 5 meteoros al principio
        x = random.randint(0, PANTALLA_TAMAÑO[0] - 100)  # Posición aleatoria en el eje X
        y = random.randint(-600, -100)  # Posición aleatoria fuera de la pantalla en el eje Y
        meteoro_rect = pygame.Rect(x, y, 50, 50)
        meteoritos.append(meteoro_rect)
        


# Función para mostrar el mensaje de Game Over y opciones de reiniciar o salir
def mostrar_game_over(puntuacion, pantalla):
    font_game_over = pygame.font.SysFont("Arial", 60)
    mensaje_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
    pantalla.blit(mensaje_game_over, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 3))


    font_reintentar = pygame.font.SysFont("Arial", 30)
    mensaje_reintentar = font_reintentar.render("Presiona R para reintentar o Q para salir", True, (255, 255, 255))
    pantalla.blit(mensaje_reintentar, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2))

    pygame.display.flip()


    # Pedir nombre del jugador
    font_nombre = pygame.font.SysFont("Arial", 30)
    texto_nombre = font_nombre.render("Ingresa tu nombre: ", True, (255, 255, 255))
    pantalla.blit(texto_nombre, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2 + 40))

    pygame.display.flip()

    # Entrada de texto del nombre
    nombre = ""
    input_active = True
    while input_active:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                input_active = False
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Al presionar "Enter" guardamos el nombre y puntuación
                    input_active = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar un caracter
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 20:  # Limitar el nombre a 20 caracteres
                        nombre += evento.unicode
        
        # Mostrar lo que el jugador ha escrito
        pantalla.fill(COLOR_CELESTE, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2 + 80, 400, 40))  # Limpiar área de entrada
        texto_nombre_ingresado = font_nombre.render(nombre, True, (255, 255, 255))
        pantalla.blit(texto_nombre_ingresado, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2 + 80))

        pygame.display.flip()

    # Guardar puntuación en el ranking
    guardar_ranking(nombre, puntuacion)
    pygame.time.delay(1000)  # Pausa antes de salir

def guardar_ranking(nombre, puntuacion):
    
        # Cargar el ranking actual desde el archivo
    with open('ranking.txt', 'r') as archivo:
        ranking = [line.strip() for line in archivo.readlines()]
        

    # Añadir la nueva puntuación con el nombre
    ranking.append(f"{nombre}: {puntuacion}")

    # Ordenar las puntuaciones de mayor a menor
    ranking = sorted(ranking, key=lambda x: int(x.split(":")[1]), reverse=True)[:10]

    # Guardar el ranking actualizado en el archivo
    with open('ranking.txt', 'w') as archivo:
        for entrada in ranking:
            archivo.write(entrada + '\n')
            
def mostrar_ranking(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion):
    input_active = True
    while input_active:
    # Mostrar el ranking en la pantalla

        # Leer el archivo de ranking (suponiendo que lo guardas en 'ranking.txt')
            with open("ranking.txt", "r") as archivo:
                rankings = archivo.readlines()  # Leer todas las líneas del archivo
                rankings = [line.strip() for line in rankings]  # Eliminar saltos de línea y espacios

            pantalla.fill(COLOR_CELESTE)  # Fondo azul

            # Título de Ranking
            font_ranking_title = pygame.font.SysFont("Arial", 40)
            texto_ranking_title = font_ranking_title.render("Ranking de Puntajes", True, (255, 255, 255))
            pantalla.blit(texto_ranking_title, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 10))

            # Mostrar los primeros 5 jugadores del ranking
            font_ranking = pygame.font.SysFont("Arial", 30)
            for i, jugador in enumerate(rankings[:5]):  # Mostrar solo los 5 primeros
                texto_jugador = font_ranking.render(f"{i+1}. {jugador}", True, (255, 255, 255))
                pantalla.blit(texto_jugador, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 5 + i * 40))

            # Instrucciones para volver
            texto_volver = font_ranking.render("Presiona ESC para volver al menú.", True, (255, 255, 255))
            pantalla.blit(texto_volver, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2 + 150))

            pygame.display.flip()  # Actualizar pantalla

            # Eventos para las instrucciones
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    input_active = False
                    pygame.quit()
                    return

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:  # Volver al menú
                        mostrar_menu(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)
        
    

def mostrar_menu(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion):
    menu_activo = True
    while menu_activo:
        pantalla.fill(COLOR_CELESTE)  # Fondo azul

        # Mensaje del título
        font_titulo = pygame.font.SysFont("Arial", 60)
        titulo = font_titulo.render("JUEGO UTN", True, (255, 255, 255))
        pantalla.blit(titulo, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 3))

        # Opciones del menú
        font_opciones = pygame.font.SysFont("Arial", 40)
        jugar = font_opciones.render("1. Jugar", True, (255, 255, 255))
        instrucciones = font_opciones.render("2. Instrucciones", True, (255, 255, 255))
        ranking = font_opciones.render("3. Ranking", True, (255, 255, 255))
        salir = font_opciones.render("4. Salir", True, (255, 255, 255))

        pantalla.blit(jugar, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 2))
        pantalla.blit(instrucciones, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 2 + 60))
        pantalla.blit(ranking, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 2 + 120))
        pantalla.blit(salir, (PANTALLA_TAMAÑO[0] // 3, PANTALLA_TAMAÑO[1] // 2 + 180))

        pygame.display.flip()  # Actualizar pantalla

        # Eventos del menú
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                menu_activo = False
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:  # Opción "Jugar"
                    menu_activo = False
                    juego(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)  # Iniciar el juego
                elif evento.key == pygame.K_2:  # Opción "Instrucciones"
                    mostrar_instrucciones(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)
                elif evento.key == pygame.K_3:  # Opción "Ranking"
                    mostrar_ranking(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)
                elif evento.key == pygame.K_4:  # Opción "Salir"
                    menu_activo = False
                    pygame.quit()

    
# Función para mostrar las instrucciones

                    
def mostrar_instrucciones(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion):
    instrucciones_activo = True
    while instrucciones_activo:
        pantalla.fill(COLOR_CELESTE)  # Fondo azul

        # Mensaje de instrucciones
        font_instrucciones = pygame.font.SysFont("Arial", 30)
        texto_instrucciones = font_instrucciones.render("Usa las teclas de dirección para mover la nave.", True, (255, 255, 255))
        pantalla.blit(texto_instrucciones, (PANTALLA_TAMAÑO[0] // 6, PANTALLA_TAMAÑO[1] // 3))

        texto_instrucciones2 = font_instrucciones.render("El juego termina si eres impactado.", True, (255, 255, 255))
        pantalla.blit(texto_instrucciones2, (PANTALLA_TAMAÑO[0] // 6, PANTALLA_TAMAÑO[1] // 3 + 40))

        # Volver al menú
        texto_volver = font_instrucciones.render("Presiona ESC para volver al menú.", True, (255, 255, 255))
        pantalla.blit(texto_volver, (PANTALLA_TAMAÑO[0] // 4, PANTALLA_TAMAÑO[1] // 2))

        pygame.display.flip()  # Actualizar pantalla

        # Eventos para las instrucciones
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                instrucciones_activo = False
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Volver al menú
                    instrucciones_activo = False
                    mostrar_menu(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)
                    
                    




    

# Bucle principal del juego
def juego(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion):
    global meteoritos, nivel, velocidad_meteoro, tiempo_inicio, rect_nave, juego_corriendo, nave_actual

    juego_corriendo = True
    rect_nave = pygame.Rect(coordenada_nave[0], coordenada_nave[1], 30, 30)
    velocidad_nave = 5
    velocidad_meteoro = 3
    meteoritos = []
    nave_actual = nave
    contador_meteoritos_esquivados = 0  # Contador de meteoritos esquivados

    # Generar meteoros al inicio
    generar_meteoros()

    # tiempos de meteoritos
    tiempo_inicio = pygame.time.get_ticks()  # Tiempo al inicio del juego
    nivel = 1
    

    # Reproducir música
    pygame.mixer.music.play(-1)

    # Bucle principal del juego
    while juego_corriendo:
       
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Volver al menú
                    esperando_volver = False
                    mostrar_menu(nave, pantalla, nave_impactada, espacio, meteoro, puntuacion)

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
                contador_meteoritos_esquivados += 1  # Incrementar el contador de meteoritos esquivados

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
        
        # Mostrar meteoritos esquivados en la pantalla
        font_contador = pygame.font.SysFont("Arial", 30)
        texto_contador = font_contador.render(f"Meteoritos Esquivados: {contador_meteoritos_esquivados}", True, (255, 255, 255))
        pantalla.blit(texto_contador, (10, 40))  # Puedes ajustar la posición si es necesario

        # Actualizar la pantalla
        pygame.display.flip()

    # Aquí calculas la puntuación (en este caso, meteoritos esquivados)
    puntuacion = contador_meteoritos_esquivados

    # Mostrar mensaje de Game Over y pasar la puntuación
    mostrar_game_over(puntuacion, pantalla)

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
                    reiniciar_juego(nave, meteoritos, rect_nave, nivel, velocidad_meteoro, tiempo_inicio, nave_actual)
                    esperando_reinicio = False
                elif evento.key == pygame.K_q:  # Si presiona "Q" sale del juego
                    esperando_reinicio = False
                    juego_corriendo = False
