import pygame
import pygame.joystick
import sys
from script.utils import load_images, load_tile, load_image
from script.tilemap import Tilemap, small_tile

RENDER_SCALE = 2

#constantsx
SCREEN_Width = 640
SCREEN_HEIGHT = 480
HALF_SCREEN_WIDTH = SCREEN_Width // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FPS = 60

class editor:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        pygame.display.set_caption("Koakuma's Adventure editor")
        self.screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))
        #放大兩倍
        self.display = pygame.Surface((HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.assets = {
            "decor" : load_tile("tiles/decor"),
            "stone" : load_tile("tiles/stone"),
            "grass" : load_tile("tiles/grass"),
            "large_decor" : load_tile("tiles/large_decor"),
            "background": load_image("background.png"),
            "spawners" : load_tile("tiles/spawners"),
        }

        self.editor_assets = {
            "decor" : load_tile("tiles/decor"),
            "stone" : load_tile("tiles/stone"),
            "grass" : load_tile("tiles/grass"),
            "large_decor" : load_tile("tiles/large_decor"),
            "spawners" : load_tile("tiles/spawners"),
        }

        self.movements = [False,False, False, False]

        self.tilemap = Tilemap(self)
        self.tilemap.load("tests/group1/game_testing/1.pickle")
        self.camera = [0,0] #camera position = offset of everything

        self.tile_list = list(self.editor_assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.click = False
        self.right_click = False
        self.shift = False
        self.on_grid = True
    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0,0))
            self.camera[0] += (self.movements[1] - self.movements[0])*2
            self.camera[1] += (self.movements[3] - self.movements[2])*2

            self.tilemap.render(self.display, self.camera)
            mouse_pos = pygame.mouse.get_pos()  
            mouse_pos = (mouse_pos[0]//RENDER_SCALE, mouse_pos[1]//RENDER_SCALE)
            tile_pos = (int((mouse_pos[0] + self.camera[0])//self.tilemap.tile_size), int((mouse_pos[1] + self.camera[1])//self.tilemap.tile_size))
            
            if self.on_grid:
                self.display.blit(self.assets[self.tile_list[self.tile_group]][self.tile_variant], (tile_pos[0]*self.tilemap.tile_size - self.camera[0], tile_pos[1]*self.tilemap.tile_size - self.camera[1]))
            else:
                self.display.blit(self.assets[self.tile_list[self.tile_group]][self.tile_variant], (mouse_pos[0] - self.camera[0], mouse_pos[1] - self.camera[1]))   

            if self.click and self.on_grid:
                self.tilemap.tilemap[str(tile_pos[0]) + ";" + str(tile_pos[1])] = small_tile(self.tile_list[self.tile_group], self.tile_variant, tile_pos)  
            if self.right_click:
                tile_location = str(tile_pos[0]) + ";" + str(tile_pos[1])   
                if tile_location in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_location]
                for tile in self.tilemap.offgrid_tiles.copy():
                    tile_img = self.assets[tile.type][tile.variant]
                    tile_r = pygame.Rect(tile.pos[0]-self.camera[0], tile.pos[1]-self.camera[1], tile_img.get_width(), tile_img.get_height())
                    if tile_r.collidepoint(mouse_pos):
                        self.tilemap.offgrid_tiles.remove(tile)

            current_tile_image = self.editor_assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_image.set_alpha(150)

            self.display.blit(current_tile_image, (5,5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                        if not self.on_grid:
                            self.tilemap.offgrid_tiles.append(small_tile(self.tile_list[self.tile_group], self.tile_variant, (mouse_pos[0] + self.camera[0], mouse_pos[1] + self.camera[1])))
                    if event.button == 3:
                        self.right_click = True
                    if not self.shift:    
                        if event.button == 4:
                            self.tile_variant = 0
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                        if event.button == 5:
                            self.tile_variant = 0
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)   
                    else:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.editor_assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.editor_assets[self.tile_list[self.tile_group]])  
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False
                    if event.button == 3:
                        self.right_click = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movements[0] = True
                    if event.key == pygame.K_d:
                        self.movements[1] = True
                    if event.key == pygame.K_w:
                        self.movements[2] = True
                    if event.key == pygame.K_s:
                        self.movements[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                    if event.key == pygame.K_g:
                        self.on_grid = not self.on_grid
                    if event.key == pygame.K_o:
                        self.tilemap.save("tests/group1/game_testing/tilemap.pickle")
                    if event.key == pygame.K_l:
                        self.tilemap.load("tests/group1/game_testing/tilemap.pickle")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movements[0] = False
                    if event.key == pygame.K_d:
                        self.movements[1] = False
                    if event.key == pygame.K_w:
                        self.movements[2] = False
                    if event.key == pygame.K_s:
                        self.movements[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False

            self.screen.blit(pygame.transform.scale(self.display, (SCREEN_Width, SCREEN_HEIGHT)), (0,0))
            pygame.display.update()
            self.clock.tick(FPS)

editor().run()
