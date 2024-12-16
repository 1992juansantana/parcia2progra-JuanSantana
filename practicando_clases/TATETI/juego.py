import random
import pygame
from recursos import cargar_imagen

class Juego:
    def __init__(self, pantalla, nivel=1):
        self.pantalla = pantalla
        self.nivel = nivel
        self.velocidad_meteoro = 3
        self.meteoritos = []
        self.meteoritos_esquivados = 0
        self.rect_nave = pygame.Rect(300, 500, 30, 30)
        self.velocidad_nave = 5
        self.nave_actual = cargar_imagen('nave.png', (100, 100))
        self.nave_impactada = cargar_imagen('nave_impactada.png', (100, 100))
        self.meteoro_img = cargar_imagen('meteoro.png', (100, 100))
        self.espacio = cargar_imagen('espacio.png', (800, 600))
        self.generar_meteoros()

    def generar_meteoros(self):
        for _ in range(5):
            x = random.randint(0, 700)
            y = random.randint(-600, -100)
            meteoro_rect = pygame.Rect(x, y, 50, 50)
            self.meteoritos.append(meteoro_rect)

    def mover_meteoros(self):
        for meteoro_rect in self.meteoritos:
            meteoro_rect.y += self.velocidad_meteoro
            if meteoro_rect.top > 600:
                meteoro_rect.y = random.randint(-600, -100)
                meteoro_rect.x = random.randint(0, 700)
                self.meteoritos_esquivados += 1

    def colisiones(self):
        for meteoro_rect in self.meteoritos:
            if self.rect_nave.colliderect(meteoro_rect):
                self.nave_actual = self.nave_impactada
                return True  # Game Over
        return False

    def mover_nave(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect_nave.x -= self.velocidad_nave
            if self.rect_nave.left < 0:
                self.rect_nave.left = 0
        if teclas[pygame.K_RIGHT]:
            self.rect_nave.x += self.velocidad_nave
            if self.rect_nave.right > 800:
                self.rect_nave.right = 800
        if teclas[pygame.K_UP]:
            self.rect_nave.y -= self.velocidad_nave
            if self.rect_nave.top < 0:
                self.rect_nave.top = 0
        if teclas[pygame.K_DOWN]:
            self.rect_nave.y += self.velocidad_nave
            if self.rect_nave.bottom > 600:
                self.rect_nave.bottom = 600

    def actualizar(self):
        self.mover_meteoros()
        return self.colisiones()

    def dibujar(self):
        self.pantalla.fill((0, 0, 0))
        self.pantalla.blit(self.espacio, (0, 0))
        for meteoro_rect in self.meteoritos:
            self.pantalla.blit(self.meteoro_img, meteoro_rect.topleft)
        self.pantalla.blit(self.nave_actual, self.rect_nave.topleft)

        # Mostrar nivel y meteoritos esquivados
        font = pygame.font.SysFont("Arial", 30)
        texto_nivel = font.render(f"Nivel: {self.nivel}", True, (255, 255, 255))
        self.pantalla.blit(texto_nivel, (10, 10))
        texto_esquivados = font.render(f"Esquivados: {self.meteoritos_esquivados}", True, (255, 255, 255))
        self.pantalla.blit(texto_esquivados, (600, 10))

    def reiniciar(self):
        self.meteoritos.clear()
        self.generar_meteoros()
        self.meteoritos_esquivados = 0
        self.rect_nave = pygame.Rect(300, 500, 30, 30)
        self.nave_actual = cargar_imagen('nave.png', (100, 100))
        self.velocidad_meteoro = 3
        self.nivel = 1
