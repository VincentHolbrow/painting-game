import pygame
from settings import *
from canvas import Canvas
import os
from button import Button
from miscdata import *

screens = ['painting', 'gallery', 'mainmenu']

canvases = []

def canvasload():
    files = os.listdir('SavedArt')
    print (files)
    for file in files:
        print (file)
        if not file == '.DS_Store':
            canvases.append(Canvas('Square', file[len(file)-5],\
                                    pygame.image.load('SavedArt/' + file)))
    if canvases == []:
        canvases.append(Canvas('Square', len(files)-1))



class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

        # Initializing buttons
        self.nextbrush = Button((250,50), (0, (resolution[1]/5)), (0,0,0), tipnames[0])
        self.nextcol = Button((250,50), (0, (resolution[1]/5 + 70)), (0,0,0), colnames[0])
        self.quit = Button((250, 50), (middlescreen[0] - 150, middlescreen[1] + 150), (50,0,0), 'Quit')
        self.resume = Button((300, 75), (middlescreen[0] - 150, middlescreen[1] - 250), (50,0,0), 'Resume')
        self.play = Button((250, 50), (middlescreen[0] - 150, middlescreen[1]), (50,0,0), 'Play')
        self.quit2 = Button((300, 75), (middlescreen[0] - 150, middlescreen[1] - 150), (50,0,0), 'Quit to menu')
        self.sell = Button((250, 50), (resolution[0] - 275, resolution[1] - 75), (80,80,0), 'Sell Painting')

        self.activescreen = 'mainmenu'
        self.screencol = (0,0,0)
        self.gallerypos = 0
        self.money = 0
        self.renoun = 0

    def buttonupdate(self):
        self.nextbrush.update(self.screen)
        self.nextcol.update(self.screen)
        self.quit.update(self.screen)
        self.resume.update(self.screen)
        self.play.update(self.screen)
        self.quit2.update(self.screen)

    def buttonhide(self):
        self.nextbrush.hidden = True
        self.nextcol.hidden = True
        self.quit.hidden = True
        self.resume.hidden = True
        self.play.hidden = True
        self.quit2.hidden = True
        self.sell.hidden = True


    def pausetoggle(self):
        if self.activescreen != 'pausemenu':
            self.prevscreen = self.activescreen
            self.activescreen = 'pausemenu'
        else:
            self.activescreen = self.prevscreen

    def draw_gallery(self):
        chunkwidth = len(canvases)*(resolution[0]/2.5)
        chunkheight = resolution[1]/1.5
        backwall = pygame.Surface((round(len(canvases)*(resolution[0]/2.5)), round(resolution[1]/1.5)))
        floor = pygame.Surface((round(len(canvases)*(resolution[0]/2.5)), round(resolution[1]/3)))
        backwall.fill((50,50,100))
        floor.fill((30,30,60))
        for can in canvases:
            
            painting = can.image
            painting = pygame.transform.scale(painting, (round(resolution[0]/5),round(resolution[0]/5)))
            backwall.blit(painting, (chunkwidth/4*(int(can.canvasnum)+1), chunkheight/4))
        self.screen.blit(backwall, (self.gallerypos,0))
        self.screen.blit(floor, (self.gallerypos, chunkheight))

    def run(self):
        self.run = True

        canvasload()
        activecan = 0

        while self.run:
            self.clock.tick(FPS)
            self.screen.fill((self.screencol))

            canvas = canvases[activecan]
            for can in canvases:
                if not can == canvas:
                    can.edit = False

            # ----- PAINTING -----
            if self.activescreen == 'painting':
                canvas.edit = True
                tooltip = 'Press L to exit to gallery, 123 to swap canvases.'

                self.buttonhide()
                self.nextbrush.hidden = False
                self.nextcol.hidden = False
                self.sell.hidden = False
                self.sell.update(self.screen, 'Sell Painting ' + str(round(canvas.quality)) + '$')

                self.screencol = (121,62,17)

            # ----- PAUSE MENU -----
            if self.activescreen == 'pausemenu':
                canvas.edit = False
                pygame.mouse.get_rel()
                tooltip = ''

                self.buttonhide()
                self.quit2.hidden = False
                self.resume.hidden = False

                self.screencol = (30,30,30)

            # ----- GALLERY -----
            if self.activescreen == 'gallery':
                canvas.edit = False
                pygame.mouse.get_rel()
                tooltip = 'Press a/d to move, k to enter painting mode.'

                self.buttonhide()

                self.screencol = (30,30,30)
                self.draw_gallery()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    self.gallerypos -= 10
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.gallerypos += 10

            # ----- Main Menu -----
            if self.activescreen == 'mainmenu':
                canvas.edit = False
                pygame.mouse.get_rel()
                tooltip = 'For Ella <3'
                self.buttonhide()
                self.play.hidden = False
                self.quit.hidden = False

                self.screen.blit(bigfont.render('Painting Game', 10, (200,200,0)), (middlescreen[0] - 140, middlescreen[1] - 250))
                self.screencol = (30,30,30)

            # ----- Event Handling -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    for can in canvases:
                        can.saveimg()
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        canvas.saveimg()
                    if event.key == pygame.K_1:
                        activecan = 0
                    if event.key == pygame.K_2:
                        activecan = 1
                    if event.key == pygame.K_3:
                        activecan = 2
                    if event.key == pygame.K_l:
                        self.activescreen = 'gallery'
                    if event.key == pygame.K_k:
                        self.activescreen = 'painting'
                    if event.key == pygame.K_ESCAPE:
                        self.pausetoggle()
            if self.resume.clicked():
                self.pausetoggle()
            if self.nextbrush.clicked():
                canvas.cycletips(1)
                self.nextbrush = Button((250,50), (0, resolution[1]/5), (0,0,0), tipnames[canvas.tipnum])
            if self.nextbrush.rightclicked():
                canvas.cycletips(-1)
                self.nextbrush = Button((250,50), (0, resolution[1]/5), (0,0,0), tipnames[canvas.tipnum])
            if self.nextcol.clicked():
                canvas.cyclecols(1)
                self.nextcol = Button((250,50), (0, resolution[1]/5 + 70), canvas.tipcol, colnames[canvas.colnum])
            if self.nextcol.rightclicked():
                canvas.cyclecols(-1)
                self.nextcol = Button((250,50), (0, resolution[1]/5 + 70), canvas.tipcol, colnames[canvas.colnum])
            if self.quit.clicked():
                for can in canvases:
                    can.saveimg()
                self.run = False
            if self.quit2.clicked():
                self.activescreen = 'mainmenu'
            if self.play.clicked():
                self.activescreen = 'gallery'
            if self.sell.clicked():
                canvasnum = canvas.canvasnum
                canvases.remove(canvas)
                canvases.append(Canvas('Square', canvasnum))
            canvas.update(self.screen, self.renoun)
            self.screen.blit(mainfont.render(tooltip, 2, (130,130,130)), (resolution[0]-400,resolution[1]-100))
            self.buttonupdate()


            pygame.display.flip()
