import pygame

# Inicializar Pygame
pygame.init()

# Crear ventana
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

# Variables del jugador
x, y = 300, 200
vel = 5
tamaño = 40
color = (255, 100, 100)  #  Color del personaje (rojo claro)

# Control de FPS
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)  # Limita el juego a 30 FPS

    # Cerrar ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()

    #  Aumentar velocidad con Shift
    if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        velocidad_actual = vel * 2
    else:
        velocidad_actual = vel

    # Movimiento del personaje
    if teclas[pygame.K_LEFT]:
        x -= velocidad_actual
    if teclas[pygame.K_RIGHT]:
        x += velocidad_actual
    if teclas[pygame.K_UP]:
        y -= velocidad_actual
    if teclas[pygame.K_DOWN]:
        y += velocidad_actual

    #  Evitar que salga de la pantalla
    if x < 0:
        x = 0
    if x > ANCHO - tamaño:
        x = ANCHO - tamaño
    if y < 0:
        y = 0
    if y > ALTO - tamaño:
        y = ALTO - tamaño

    # Dibujar todo
    pantalla.fill((30, 30, 30))  # Fondo
    pygame.draw.rect(pantalla, color, (x, y, tamaño, tamaño))  # Jugador
    pygame.display.update()

pygame.quit()
