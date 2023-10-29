import pygame

game_size = (500, 400)
text = 'ברוך הבא אביאל'
snake_speed = 30

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

pygame.init()

displ = pygame.display.set_mode(game_size)
pygame.display.set_caption(text)
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

game_over = False
center_place = (game_size[0] // 2, game_size[1] // 2)
place = center_place
change = (0, 0)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    displ.blit(mesg, [*center_place])


def shakeGameOver(please):
    if please[0] > game_size[0] or please[1] > game_size[1] or please[0] < 0 or please[1] < 0:
        return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = (0, -10)
            if event.key == pygame.K_DOWN:
                change = (0, 10)
            if event.key == pygame.K_LEFT:
                change = (-10, 0)
            if event.key == pygame.K_RIGHT:
                change = (10, 0)
    place = (place[0] + change[0], place[1] + change[1])
    game_over = shakeGameOver(place)

    displ.fill(white)
    pygame.draw.rect(displ, blue, [*place, 10, 10])
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
quit()
