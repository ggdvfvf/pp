from pygame import *

w = 500
d = 700
win = display.set_mode((d, w))
display.set_caption('ping pong')
fon = win.fill((250,250,250))



class GSprite(sprite.Sprite):
    def __init__(self, p_image, sp_x, sp_y, x, y, sp_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (x, y))
        self.speed = sp_speed
        self.rect = self.image.get_rect()
        self.rect.x = sp_x
        self.rect.y = sp_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < w - 200:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < w - 200:
            self.rect.y += self.speed

rak1 = Player('raket.png', 10, 100, 50, 200, 5)
rak2 = Player('raket.png', 650, 100, 50, 200, 5)
ball = GSprite('ball.png', 500, 200, 50, 50, 4)
p1 = GSprite('p1.png', 200, 50, 100, 50, 0)
p2 = GSprite('p2.png', 650, 50, 100, 50, 0)

#lose = font1.render("Пропущено: " + str(lost), 1, (255,255, 255))

font.init()

font2 = font.SysFont('Arial', 40)

speed_x = 3
speed_y = 3
game = True
clock = time.Clock()
finish = False
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        win.fill((250,250,250))
        rak1.update1()
        rak1.reset()
        rak2.update2()
        rak2.reset()
        ball.reset()
        p1.reset()
        p2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rak1, ball) or sprite.collide_rect (rak2, ball):
            speed_x *= -1
            
        if ball.rect.y < 0 or ball.rect.y > w - 20:
            speed_y *= -1

        if ball.rect.x < 0:  
                finish = True                   
                text_win = font2.render("win 2", 1, (0,0, 255))
                win.blit(text_win,(300, 300))
        if ball.rect.x > 700:  
                finish = True                   
                text_win = font2.render("win 1", 1, (0,0, 255))
                win.blit(text_win,(300, 300))



    display.update()
    clock.tick(40)
    
    #мемори карт, умн заметки, редак изобр, лаб, шутер, пп