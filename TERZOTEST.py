import pygame
import random

# Inizializzazione di Pygame
pygame.init()

# Colori
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensioni della finestra
WIDTH, HEIGHT = 640, 480

# Creazione della finestra di gioco
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Velocità del serpente
snake_speed = 10

# Posizione iniziale del serpente
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Posizione iniziale del cibo
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Direzione iniziale del serpente
direction = 'RIGHT'
change_to = direction


# Funzione per il messaggio di Game Over
def message(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    win.blit(text_surf, text_rect)
    pygame.display.flip()


# Loop principale del gioco
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Cambia la direzione in modo valido
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Muovi il serpente
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Aggiungi il corpo del serpente
    snake_body.insert(0, list(snake_pos))

    # Verifica la collisione con il cibo
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]

    food_spawn = True
    win.fill(WHITE)

    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Verifica la collisione con i bordi o con il corpo
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over = True

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# Messaggio di Game Over
message("Hai perso! Premi R per giocare di nuovo o Q per uscire.", 40, RED, WIDTH / 2, HEIGHT / 2)

# Attendi l'input dell'utente per rigiocare o uscire
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_r:
                exec(open(__file__).read())