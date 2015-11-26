##Console emulator written in Pygame.
##Created 2015 Thomas Doylend
##

import pygame; pygame.init()

color = [
    (000,000,000),(000,000,128),(000,128,000),(000,128,128),
    (128,000,000),(128,000,128),(128,128,000),(192,192,192),
    (128,128,128),(000,000,255),(000,255,000),(000,255,255),
    (255,000,000),(255,000,255),(255,255,000),(255,255,255)
    ]

class Console:
    def __init__(self,title="Console",fullscreen=False):
        self.display = pygame.display.set_mode((640,480),pygame.FULLSCREEN&fullscreen)
        pygame.display.set_caption(title)

        self.surf = pygame.Surface((640,480))

        self.font = pygame.image.load('font.png')
        self.font.set_colorkey((255,255,255))
        self.fonts = []

        for color_item in color:
            new_font = pygame.Surface((2048,12))
            new_font.fill(color_item)
            new_font.blit(self.font,(0,0))
            new_font.set_colorkey((0,0,64))
            self.fonts.append(new_font)

        self.fg = 7
        self.bg = 0

        self.keys = []
        
    def clear(self):
        self.surf.fill(color[self.bg])
        
    def char(self,x,y,char):
        pygame.draw.rect(self.surf,color[self.bg],(x*8,y*12,8,12))
        self.surf.blit(self.fonts[self.fg].subsurface((ord(char)*8,0,8,12)),
                       (x*8,y*12))

    def getkey(self):
        if self.keys: return self.keys.pop(0)
        else: return None

    def update(self):
        self.display.blit(self.surf,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keys.append(event.unicode)
                if event.key == pygame.K_ESCAPE: self.keys.append(chr(27))
                elif event.key == pygame.K_UP: self.keys.append(chr(192))
                elif event.key == pygame.K_DOWN: self.keys.append(chr(193))
                elif event.key == pygame.K_LEFT: self.keys.append(chr(194))
                elif event.key == pygame.K_RIGHT: self.keys.append(chr(195))
                elif event.key == pygame.K_BACKSPACE: self.keys.append(chr(200))
            elif event.type == pygame.QUIT:
                self.keys.append(chr(27))
        pygame.display.update()

    def rect(self,start_x,start_y,width,height):
        for x in xrange(start_x,start_x+width):
            self.char(x,start_y,chr(205))
            self.char(x,start_y+height-1,chr(205))
        for y in xrange(start_y,start_y+height):
            self.char(start_x,y,chr(186))
            self.char(start_x+width-1,y,chr(186))
        self.char(start_x,start_y+height-1,chr(200))
        self.char(start_x+width-1,start_y+height-1,chr(188))
        self.char(start_x,start_y,chr(201))
        self.char(start_x+width-1,start_y,chr(187))
    
    def horiz_div(self,start_x,start_y,width):
        for x in xrange(start_x,start_x+width):
            self.char(x,start_y,chr(205))
        self.char(start_x,start_y,chr(204))
        self.char(start_x+width-1,start_y,chr(185))
    
    def string(self,x,y,string):
        for count in xrange(len(string)):
            self.char(x+count,y,string[count])
