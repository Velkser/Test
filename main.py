
import pygame
def move_player():
  player.y += player_speed
  if player.top <= 0:
    player.top = 0
  if player.bottom >= SCREEN_HEIGHT:
    player.bottom = SCREEN_HEIGHT
    
def move_ball(dx, dy):
  if ball.top <=0 or ball.bottom >= SCREEN_HEIGHT:
    dy = -dy
  if ball.colliderect(player) or ball.colliderect(bot):
    dx = -dx
  now = pygame.time.get_ticks()
  if now - score_time >= pause:
    ball.x += dx
    ball.y += dy
  return dx, dy

def print_message(message, x ,y,  font_color=(0,0,0), font_type = "text/LEMONMILK-Regular.otf", font_size = 30):
  font_type = pygame.font.Font(font_type, font_size)
  text = font_type.render(message, True, font_color)
  screen.blit(text, (x, y))

def move_bot():
  if ball.centerx > SCREEN_WIDTH/2 and ball_dx>0:
    if ball.bottom < bot.top:
      bot.y -= 5
    if ball.top > bot.bottom:
      bot.y +=5
    
    
def restart():
  ball.center = SCREEN_WIDTH/2 , SCREEN_HEIGHT/2


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 350
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG_COLOR = (0, 255, 128)
YELLOW = (255, 255, 0)

run = True
scren_res = (SCREEN_WIDTH, SCREEN_HEIGHT)
x = 50
y = 50
player = pygame.Rect(10, SCREEN_HEIGHT/2 - 50, 15, 100)
bot = pygame.Rect(SCREEN_WIDTH -25, SCREEN_HEIGHT/2 - 50, 15, 100)
ball = pygame.Rect(SCREEN_WIDTH/2 -10, SCREEN_HEIGHT/2 +10, 20, 20)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(scren_res)
pygame.display.set_caption("My game")

player_speed = 0


pause = 1500
score_time = 0

ball_dx = -5
ball_dy = +5

while run:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 5
            elif event.key == pygame.K_s:
                player_speed += 5
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 5
            elif event.key == pygame.K_s:
                player_speed -= 5

  move_player()
  move_bot()
  ball_dx, ball_dy = move_ball(ball_dx, ball_dy)
  if ball.left > SCREEN_WIDTH or ball.right < 0:
    restart()
    score_time = pygame.time.get_ticks()
    
    
  screen.fill(BG_COLOR)
  pygame.draw.rect(screen, BLUE , player)
  pygame.draw.rect(screen, RED , bot)
  pygame.draw.ellipse(screen, YELLOW, ball )
  pygame.draw.line(screen, YELLOW, (SCREEN_WIDTH/2, 0),(SCREEN_WIDTH/2, SCREEN_HEIGHT))
  
  clock.tick(70)
  pygame.display.flip()
pygame.quit()


