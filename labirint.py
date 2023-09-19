from pygame import *
class all(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(all):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if self.rect.x > 0 and self.x_speed<0 or self.rect.x < 620 and self.x_speed>0:
            self.rect.x += self.x_speed
        if self.rect.y > 0 and self.y_speed<0 or self.rect.y < 420 and self.y_speed>0:
            self.rect.y += self.y_speed
    def shoot(self):
        bull = Bullet('bullet.png', 40, 10, self.rect.x+20, self.rect.y+20, 0, 0)
        bullets.add(bull)
        if e.key == K_w:
            bull.y_speed = -20
        elif e.key == K_s:
            bull.y_speed = 20
        elif e.key == K_d:
            bull.x_speed = 20
        elif e.key == K_a:
            bull.x_speed = -20      
class Bullet(all):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if sprite.spritecollide(self, walls, False):
            self.kill()
window = display.set_mode((700, 500))
window.fill((0, 125, 126))
display.set_caption('labirint')
run = True
blue = (0, 125, 125)
wight =700
haight = 500
player2 = player('1-2.png', 80, 80, 0, 0, 0, 0)
enemy  = player('cyborg.png', 80, 80, 349, 300, 0, 0)
wall1 = all('123.png', 20, 380, 300, 30)
wall2 = all('123.png', 200, 20, 300, 30)
wall3 = all('123.png', 300, 20, 200, 180)
fin = all('trophy.png', 80, 80, 620, 0)
lost = all('game-over_1.png', 700, 500, 0, 0)
walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
finish = False
touch = True
count = 1
bullets = sprite.Group()
enemys = sprite.Group()
enemys.add(enemy)
ret = False
while run:
    while run and  not finish and touch: 
        ret = True
        window.fill((0, 125, 126))
        player2.reset()
        enemys.draw(window) 
        walls.draw(window) 
        fin.reset()
        bullets.draw(window)  
        for e in event.get():
            if e.type ==QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    player2.y_speed = -5
                elif e.key == K_DOWN:
                    player2.y_speed = 5
                elif e.key == K_RIGHT:
                    player2.x_speed = 5 
                elif e.key == K_LEFT:
                    player2.x_speed = -5
                elif e.key == K_w:
                    player2.shoot()
                elif e.key == K_s:
                    player2.shoot()   
                elif e.key == K_d:
                    player2.shoot()
                elif e.key == K_a:
                    player2.shoot()        
            elif e.type == KEYUP:
                if e.key == K_UP:
                    player2.y_speed = 0   
                elif e.key == K_DOWN:
                    player2.y_speed = 0    
                elif e.key == K_RIGHT:
                    player2.x_speed = 0     
                elif e.key == K_LEFT:
                    player2.x_speed = 0            
        player2.update()
        bullets.update()
        if enemy.rect.x < 350:
            enemy.x_speed = 7
        if enemy.rect.x > 620:
            enemy.x_speed = -7
        enemys.update()
        if sprite.collide_rect(player2, enemy):
            touch = False
        if sprite.spritecollide(player2, walls, False):
            touch = False
        if player2.rect.x == fin.rect.x and player2.rect.y == fin.rect.y:
            finish= True
        if sprite.groupcollide(enemys, bullets, True, True):
            enemy.rect.y = -500
            enemy.kill()
        time.delay(50)
        display.update()  
    while (run or finish) and ret:  
        if finish:
            window.fill((0, 125, 126))
            fin = all('trophy.png', 700, 500, 0, 0)
            fin.reset() 
        else:
            lost.reset()
                
        for e in event.get():
            if e.type ==QUIT:
                    run = False
                    finish = False
            elif e.type == KEYDOWN:
                    if e.key == K_w:
                        ret = False
                        touch = True
                        finish = False
                        player2.rect.x = 0
                        player2.rect.y = 0
                        player2.x_speed = 0
                        player2.y_speed = 0


        time.delay(50)
        display.update()
