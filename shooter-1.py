from pygame import *

window=display.set_mode((700,500))
display.set_caption('SHOOTER')
backgrond=transform.scale(image.load('galaxy.jpg'),(700,500))

clock=time.Clock()
mixer.init()
mixer.music.load('space.ogg')
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self,o_image,sprite_x,sprite_y,width,height,speed):
        super().__init__()
        self.speed=speed
        self.image=transform.scale(image.load(o_image),(width,height))

        self.rect=self.image.get_rect()
        self.rect.x=sprite_x
        self.rect.y=sprite_y

    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        pass

    def fire(self):
        pass
    def fire2(self):
        pass


player=Player('rocket.png',200,390,80,100,5)

run=True
finish=False
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
    
    if not finish:
        window.blit(backgrond,(0,0))
        player.draw()
        player.update()
    




    display.update()
    clock.tick(60)
