import pygame
from settings import *
pygame.init()

class instance():
    def __init__(self, launchOptions):
        #-------------- Setting up Base Parameters ----------------------------
        self.res = launchOptions['resolution']
        self.gamestate = ['menu', 'main']
        self.screen = pygame.display.set_mode(self.res)


        #-------------- Setting up Gamestate ----------------------------------
        # defining gamestate functions
        def paintloop(self, params):
            pass

        def menuloop(self, params):
            menu = params[0]
            print(menu)
            buttons = self.menus[menu]
            for button in buttons:
                text = button[0]
                size = button[1]
                position = button[2]
                colour = button[3]
                font = pygame.font.SysFont('Comic Sans MS', round(size[1]/2))

                base = pygame.Surface(size)
                base.fill((255,255,255))
                base.blit(font.render(text, True, (0,0,0)), (0,size[1]/8))
                trueposition = position[0] - size[0]/2, position[1] - size[1]/2
                self.screen.blit(base, (trueposition))

        def galleryloop(self, params):
            pass
        

        #-------------- Setting up Dictionaries -------------------------------
        # assigning gamestates to dict
        self.gamestates = {
            'paint': paintloop,
            'menu': menuloop,
            'gallery': galleryloop,
        }

        self.menus = {
            # 'menu' is a list of buttons
            'main':[
                # button format is [text, (sizex,sizey), (posx,posy), (r,g,b)]
                ['New', (self.res[0]/8, self.res[1]/8), (middlescreen), (255,255,255)]
            ] 
        }


    def run(self):
        self.run = True


        while self.run:
            self.screen.fill((0,0,0))
            parameters = []
            for i in (self.gamestate):
                if not self.gamestate.index(i) == 0:
                    parameters.append(i)
            self.gamestates['menu'](self, parameters)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.flip()

game = instance(launchOptions)
game.run()