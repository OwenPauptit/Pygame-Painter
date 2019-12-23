import pygame

class BrushObject:
    def __init__(self):
        self.colour = (0,0,0)
        self.size = 8
    def paint(self,x,y,screen):        
        pygame.draw.rect(screen,self.colour,(x-self.size/2,y-self.size/2,self.size,self.size))
    def change_colour(self,colour):
        if colour == 0:
            self.colour = (233,10,10) #red
        elif colour == 1:
            self.colour = (10,36,233) #blue
        elif colour == 2:
            self.colour = (67,218,37) #green
        elif colour == 3:
            self.colour = (255,255,255) #white
        else:
            self.colour = colour
        
class Overlay:
    def __init__(self):
        self.image = pygame.image.load("Full Overlay.png")
        self.slider = pygame.image.load("Slider.png")
        self.sliderpos = self.image.get_rect()
        self.sliderpos.center = (866,452)
        self.buttons = [35,87,[36,128,221,320],[120,212,304,383]] # in form [top,bottom,left,right]
    def is_button(self,x,y):
        if y > self.buttons[0] and y < self.buttons[1]:
            for i in range(0,4):
                if x > self.buttons[2][i] and x < self.buttons[3][i]:
                    return i
        return -1

    def is_slider(self,x,y):
        if y > 48 and y < 74:
            if x > 438 and x < 750:
                self.sliderpos.centerx = x + 395
                return round(((x - 428) / 10),0)
        return -1
                
        


def main():
    brush = BrushObject()
    background = Overlay()

    screen = pygame.display.set_mode((800,800))
    screen.fill((255,255,255))

    mousedown = False

    while True:
        Rect = (background.sliderpos.left,background.sliderpos.top,20,20)
        pygame.draw.rect(screen,(255,255,255),Rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
                
            if mousedown == True:            
                x,y = pygame.mouse.get_pos()

                if background.is_button(x,y) != -1:
                    brush.change_colour(background.is_button(x,y))
                elif background.is_slider(x,y) != -1:
                    brush.size = background.is_slider(x,y)
                else:                
                    brush.paint(x,y,screen)
        screen.blit(background.image,(0,0))
        screen.blit(background.slider,background.sliderpos)
        pygame.display.update()

main()
