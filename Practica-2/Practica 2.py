import pygame
pygame.init()

# Ventana
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Práctica 2 - Saltos y Gravedad")

# Variables del jugador
x, y = 300, 300
vel_y = 0
gravedad = 1
fuerza_salto = 17  #  fuerza del salto
en_suelo = True
saltos_realizados = 0  #  para controlar doble salto

# Control de FPS
clock = pygame.time.Clock()
running = True

# Suelo visible
suelo_y = 340  # posición del suelo

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    #  Saltar o doble salto
    if teclas[pygame.K_SPACE]:
        if en_suelo:  # primer salto
            vel_y = -fuerza_salto
            en_suelo = False
            saltos_realizados = 1
        elif saltos_realizados == 1:  # segundo salto
            vel_y = -fuerza_salto
            saltos_realizados = 2

    # Movimiento vertical
    y += vel_y
    vel_y += gravedad

    # Detectar suelo
    if y >= suelo_y:
        y = suelo_y
        vel_y = 0
        en_suelo = True
        saltos_realizados = 0  # reiniciar saltos al tocar suelo

    # Dibujar escena
    pantalla.fill((50, 50, 100))  # fondo
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))  # jugador
    pygame.draw.rect(pantalla, (0, 255, 0), (0, suelo_y + 40, ANCHO, 60))  # suelo visible
    pygame.display.update()

pygame.quit()
