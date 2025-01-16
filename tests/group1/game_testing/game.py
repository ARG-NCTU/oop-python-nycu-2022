import pygame
import pygame.joystick
import sys
import os
import random
import math
from script.entity import physics_entity, Player, Enemy, Diagnal_Projectile
from script.utils import load_image
from script.utils import load_tile
from script.utils import load_images
from script.utils import load_trans_images,load_trans_image
from script.utils import load_sfx
from script.utils import Animation
from script.tilemap import Tilemap, small_tile
from script.particle import Particle
from script.spark import Spark, Flame, Ice_Flame, Gold_Flame, Dark_Blue_Flame,Flexible_Spark    

#constants
SCREEN_Width = 640
SCREEN_HEIGHT = 480
SCREEN_Width = 1280
SCREEN_HEIGHT = 960
HALF_SCREEN_WIDTH = SCREEN_Width // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FPS = 60

class main_game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        pygame.display.set_caption("Koakuma's Adventure")
        self.screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT),pygame.SRCALPHA)
        #放大兩倍
        self.display = pygame.Surface((HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT), pygame.SRCALPHA)
        self.display_for_outline = pygame.Surface((HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
        self.display_pause = pygame.Surface((SCREEN_Width, SCREEN_HEIGHT),pygame.SRCALPHA)

        self.clock = pygame.time.Clock()
        self.pause = False
        self.pause_select = 0
        self.pause_select_cd = 0

        self.movements = [False,False]

        self.assets = {
            "decor" : load_tile("tiles/decor"),
            "stone" : load_tile("tiles/stone"),
            "grass" : load_tile("tiles/grass"),
            "large_decor" : load_tile("tiles/large_decor"),
            "player": load_image("entities/player.png"),
            "background": load_image("background.png"),
            "enemy/idle" : Animation(load_images("entities/enemy/idle"),duration=6,loop=True),
            "enemy/run" : Animation(load_images("entities/enemy/run"),duration=4,loop=True),
            "player/idle" : Animation(load_trans_images("entities/player/idle"),duration=10,loop=True),
            "player/run" : Animation(load_trans_images("entities/player/run"),duration=4,loop=True),
            "player/jump" : Animation(load_trans_images("entities/player/jump"),duration=5,loop=True),
            "particle/leaf" : Animation(load_images("particles/leaf"),duration=20,loop=False),
            "particle/particle" : Animation(load_images("particles/particle"),duration=6,loop=False),
            "gun" : load_image("gun.png"),
            "projectile" : load_image("projectile.png"),
            "projectile_1": load_image("projectile.png"),
            "projectile_2": load_image("projectile_orange.png"),
            "projectile_3": load_image("projectile_yellow.png"),
            "projectile_4": load_image("projectile_green.png"), 
            "projectile_5": load_image("projectile_aqua.png"),  
            "projectile_6": load_image("projectile_blue.png"),
            "projectile_7": load_image("projectile_purple.png"),
            "HP" : load_trans_image("HP.png"),
            "Boss_full" : load_trans_image("max_HP_bar.png"),
            "Boss_empty" : load_trans_image("empty_HP_bar.png"),
            "retry" : load_image("buttons/retry_1.png"),  
            "pressed_retry" : load_image("buttons/retry_2.png"),

        }

        self.sfx = {
            "jump" : load_sfx("jump.wav"),
            "dash" : load_sfx("dash.wav"),
            "shoot" : load_sfx("shoot.wav"),
            "hit" : load_sfx("hit.wav"),
            "got_hit" : load_sfx("player_take_damage.wav"),
            "ambience" : load_sfx("ambience.wav"),
            "swing" : load_sfx("swing.wav"),
        }   
        self.sfx["ambience"].set_volume(0.2)
        self.sfx["shoot"].set_volume(0.5)
        self.sfx["jump"].set_volume(0.7)
        self.sfx["dash"].set_volume(0.7)
        self.sfx["swing"].set_volume(0.7)
        self.sfx["hit"].set_volume(0.8) 
        self.sfx["got_hit"].set_volume(1)


        self.level = 0
        self.load_level()

    def load_level(self,new_level=True):

        self.player = Player(self, (100,100), (8,15) , HP = 5)

        self.tilemap = Tilemap(self)

        self.projectiles = []
        self.special_projectiles = [] #object [pos,direction,speed,timer,img_name]
        self.particles = []
        self.sparks = []
        self.buffer = []    

        self.camera = [0,0] #camera position = offset of everything
        self.min_max_camera = [0,0] #min and max camera x position
        self.screen_shake_timer = 0
        self.screen_shake_offset = [0,0]
        self.dead = 0 #dead animation

        self.tilemap.load("tests/group1/game_testing/"+str(self.level)+".pickle")

        self.leaf_spawners = []

        for tree in self.tilemap.extract([('large_decor',2)],keep=True):
            self.leaf_spawners.append(pygame.Rect(4+tree.pos[0], 4+tree.pos[1], 23, 13))

        self.enemy_spawners = []
        for spawner in self.tilemap.extract([('spawners',0),('spawners',1)],keep=False):
            if spawner.variant == 0:
                self.player.position = spawner.pos #player start position
            else:
                self.enemy_spawners.append(Enemy(self,spawner.pos,(8,15),phase=1))

        if self.level == 0:
            self.transition = -30
        elif self.level == 1:
            self.transition = -50
        self.win = 0

        if self.level == 0:
            if new_level:
                pygame.mixer.music.load("tests/group1/game_testing/data/sfx/music_1.wav")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)

            
        elif self.level == 1:
            if new_level:
                pygame.mixer.music.load("tests/group1/game_testing/data/sfx/music.wav")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

    def run(self):

        #self.sfx["ambience"].play(-1)
        while True:
            while self.pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.pause = False
                            pygame.mixer.music.set_volume(0.2)
                        if event.key == pygame.K_UP and self.pause_select_cd == 0:
                            self.pause_select = max(0,self.pause_select-1)
                            self.pause_select_cd = 1
                        if event.key == pygame.K_DOWN and self.pause_select_cd == 0:
                            self.pause_select = min(1,self.pause_select+1)
                            self.pause_select_cd = 1
                        if event.key == pygame.K_SPACE:
                            if self.pause_select == 0:
                                self.pause = False
                                pygame.mixer.music.set_volume(0.2)
                            else:
                                self.pause = False
                                pygame.mixer.music.set_volume(0.2)
                                self.dead = 10
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 11:
                            self.pause = False
                            pygame.mixer.music.set_volume(0.2)
                        if event.button == 0:
                            if self.pause_select == 0:
                                self.pause = False
                                pygame.mixer.music.set_volume(0.2)  
                            else:
                                self.pause = False
                                self.dead = 10
                                pygame.mixer.music.set_volume(0.2)
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 1:
                            if event.value < -0.5 and self.pause_select_cd == 0:
                                self.pause_select = max(0,self.pause_select-1)
                                self.pause_select_cd = 1
                            elif event.value > 0.5 and self.pause_select_cd == 0:
                                self.pause_select = min(1,self.pause_select+1)
                                self.pause_select_cd = 1
                
                #make self.display_pause a transparent screen
                self.pause_select_cd = max(0,self.pause_select_cd-1)
                self.display_pause.fill((0, 0, 0, 0))   
                self.display_pause.blit(self.assets['retry'], (SCREEN_Width//16 - self.assets['retry'].get_width()//2, SCREEN_HEIGHT//16-18 - self.assets['retry'].get_height()//2))
                self.display_pause.blit(self.assets['retry'], (SCREEN_Width//16 - self.assets['retry'].get_width()//2, SCREEN_HEIGHT//16 - self.assets['retry'].get_height()//2))
                if self.pause_select == 0:
                    self.display_pause.blit(self.assets['pressed_retry'], (SCREEN_Width//16 - self.assets['pressed_retry'].get_width()//2, SCREEN_HEIGHT//16-18 - self.assets['pressed_retry'].get_height()//2))
                else:
                    self.display_pause.blit(self.assets['pressed_retry'], (SCREEN_Width//16 - self.assets['pressed_retry'].get_width()//2, SCREEN_HEIGHT//16 - self.assets['pressed_retry'].get_height()//2))


                self.screen.blit(pygame.transform.scale(self.display_pause, (8*SCREEN_Width, 8*SCREEN_HEIGHT)), self.screen_shake_offset) 
                pygame.display.update()
                self.clock.tick(FPS)


            self.display.fill((0,0,0,0))
            self.display_for_outline.blit(self.assets['background'], (0,0))

            if self.transition < 0:
                self.transition += 1
            if self.win>0:
                self.win += 1
                pygame.mixer.music.set_volume(0.2*(90-self.win)/90)
                if self.win > 90:
                    self.transition += 1
                    if self.transition > 30:
                        self.level += 1
                        self.load_level()

            if self.dead > 0:
                self.dead += 1
                if self.dead >=10:
                    self.transition = min(30,self.transition+1)
                if self.dead > 40:
                    self.load_level(False)

            self.camera[0] += (self.player.rect().centerx - self.display.get_width()/2 -self.camera[0])/20 #camera follow player x
            self.camera[0] = min(self.min_max_camera[0],self.camera[0])
            self.camera[0] = max(self.min_max_camera[1],self.camera[0])
            #self.camera[1] += (self.player.rect().centery - self.display.get_height()/2 - self.camera[1])/20 #camera follow player y
            self.render_camera = [int(self.camera[0]), int(self.camera[1])]

            for spawner in self.leaf_spawners:
                if random.random() * 49999 < spawner.width* spawner.height:
                    pos = (spawner.x + random.random()*spawner.width, spawner.y + random.random()*spawner.height)
                    self.particles.append(Particle(self,'leaf',pos,velocity=[-0.1,0.3],frame=random.randint(0,20)))
            self.tilemap.render(self.display,offset=self.render_camera) #render background

            for enemy in self.enemy_spawners.copy():
                kill = enemy.update((0,0),self.tilemap)
                enemy.render(self.display,offset=self.render_camera)
                if kill:
                    self.projectiles=[] 
                    self.special_projectiles=[]
                    phase = enemy.phase
                    self.enemy_spawners.remove(enemy)
                    for i in range(4):
                        self.sparks.append(Flame((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 3+random.random()))
                        self.sparks.append(Flexible_Spark((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 3+random.random(),(255,127,0)))
                        self.sparks.append(Gold_Flame((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 2+random.random()))
                        self.sparks.append(Flexible_Spark((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 1+random.random(),(0,255,0)))
                        self.sparks.append(Ice_Flame((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 5+random.random()))
                        self.sparks.append(Flexible_Spark((enemy.rect().center[0]+random.randint(-8,8),enemy.rect().center[1]), 1.5*math.pi, 4+random.random(),(148,0,211)))
                    if phase == 1:
                        self.enemy_spawners.append(Enemy(self,[287,145],(8,15),phase=2,action_queue=[100,"jump()",40,"frozen_in_air()",10,"air_8_shoot(1)",30,"air_8_shoot(2)",30,"air_8_shoot(1)",30,"prepare_attack()",["attack_preview()",30],5,["dash_to()",1]]))
                    elif phase == 2:
                        self.enemy_spawners.append(Enemy(self,[287,90],(8,15),phase=3,action_queue=[60,"prepare_attack(1)",60,["spell_card()",80],90,"air_dash()",40,"frozen_in_air()",10,["spell_card()",80],90,["spread()",15],90,"prepare_attack()",["attack_preview()",30],5,["dash_to()",1]]))
                    elif phase == 3:
                        self.first_phase_cutscene()
                        self.win = 1
            if not self.dead:
                self.player.update((self.movements[1] - self.movements[0],0),self.tilemap) #update player
                #self.player.render(self.display,offset=self.render_camera) #render player
                


            self.max_jump_height = -3  # Maximum jump velocity
            self.min_jump_height = -1   # Minimum jump velocity
            self.jump_start_time = None

            #[[x,y],direction,timer]
            for projectile in self.projectiles.copy():
                projectile[0][0] += projectile[1]
                projectile[2] += 1
                img = self.assets['projectile']
                self.display.blit(img,(projectile[0][0]-img.get_width()/2 -self.render_camera[0],projectile[0][1]-img.get_height()/2-self.render_camera[1]))
                if self.tilemap.solid_check(projectile[0]):
                    try:
                        self.projectiles.remove(projectile) 
                    except:
                        pass
                    for i in range(4):
                        self.sparks.append(Spark(projectile[0],random.random()*math.pi*2,2+random.random()))
                elif projectile[2] > 360:
                    try:
                        self.projectiles.remove(projectile)
                    except:
                        pass
                elif abs(self.player.dashing) < 50:
                    if self.player.rect().collidepoint(projectile[0]):
                        try:
                            self.projectiles.remove(projectile)
                        except:
                            pass
                        self.player.take_damage(1,(list(self.player.rect().center).copy()[0]-projectile[0][0],0))
            for special_projectile in self.special_projectiles.copy():
                special_projectile.update()
                img = self.assets[special_projectile.img_name]
                #rotate image according to its direction which is a vector
                angle = math.atan2(special_projectile.direction[1],special_projectile.direction[0]) * 180 / math.pi
                #img = pygame.transform.rotate(img,-1*angle)
                self.display.blit(img,(special_projectile.pos[0]-img.get_width()/2 -self.render_camera[0],special_projectile.pos[1]-img.get_height()/2-self.render_camera[1]))
                if self.tilemap.solid_check(special_projectile.pos):
                    try:
                        self.special_projectiles.remove(special_projectile)
                    except:
                        pass
                    for i in range(4):
                        #match the spark's color with the projectile
                        if special_projectile.img_name == 'projectile_1':
                            self.sparks.append(Flame(special_projectile.pos,random.random()*math.pi*2,2+random.random()))
                        elif special_projectile.img_name == 'projectile_2':
                            self.sparks.append(Flexible_Spark(special_projectile.pos,random.random()*math.pi*2,2+random.random(),(255,127,0)))
                        elif special_projectile.img_name == 'projectile_3':
                            self.sparks.append(Gold_Flame(special_projectile.pos,random.random()*math.pi*2,2+random.random()))
                        elif special_projectile.img_name == 'projectile_4':
                            self.sparks.append(Flexible_Spark(special_projectile.pos,random.random()*math.pi*2,2+random.random(),(0,255,0)))
                        elif special_projectile.img_name == 'projectile_5':
                            self.sparks.append(Ice_Flame(special_projectile.pos,random.random()*math.pi*2,2+random.random()))
                        elif special_projectile.img_name == 'projectile_6':
                            self.sparks.append(Flexible_Spark(special_projectile.pos,random.random()*math.pi*2,2+random.random(),(148,0,211)))
                        elif special_projectile.img_name == 'projectile_7':
                            self.sparks.append(Flexible_Spark(special_projectile.pos,random.random()*math.pi*2,2+random.random(),(255,0,255)))
                        else:
                            self.sparks.append(Spark(special_projectile.pos,random.random()*math.pi*2,2+random.random()))   
                elif special_projectile.timer > 360:
                    try:
                        self.special_projectiles.remove(special_projectile) 
                    except:
                        pass    
                elif abs(self.player.dashing) < 50: 
                    if self.player.rect().collidepoint(special_projectile.pos):
                        try:
                            self.special_projectiles.remove(special_projectile)
                        except:
                            pass
                        self.player.take_damage(1,(list(self.player.rect().center).copy()[0]-special_projectile.pos[0],0))

            for spark in self.sparks.copy():
                kill = spark.update()
                spark.render(self.display,offset=self.render_camera)
                if kill:
                    self.sparks.remove(spark)   

            display_mask = pygame.mask.from_surface(self.display)
            display_sillouette = display_mask.to_surface(setcolor=(0,0,0,180),unsetcolor=(0,0,0,0))
            #outline stuff but I dont like it
            #for offset in [[-1,0],[1,0],[0,1],[0,-1]]:
            #    self.display_for_outline.blit(display_sillouette,offset)

            for particle in self.particles.copy():
                kill = particle.update()
                if particle.p_type == 'leaf':
                    particle.pos[0] += math.sin(particle.animation.frame*0.035)*0.3
                particle.render(self.display,offset=self.render_camera)
                if kill:
                    self.particles.remove(particle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = True
                    if event.key == pygame.K_UP:
                        self.player.jump()
                    if event.key == pygame.K_SPACE:
                        self.player.dash()
                    if event.key == pygame.K_z: 
                        self.player.attack()
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.movements = [False,False]  
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = False

                #joystick control
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        if event.value < -0.3:
                            self.movements[0] = True
                            self.movements[1] = False
                        elif event.value > 0.3:
                            self.movements[1] = True
                            self.movements[0] = False
                        else:
                            self.movements[0] = False
                            self.movements[1] = False

                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        if not self.player.jump():
                            self.buffer=["jump",6]
                    if event.button == 7:
                        if not self.player.dash():
                            self.buffer=["dash",6]
                    if event.button == 3:
                        if not self.player.attack():
                            self.buffer=["attack",6]
                    if event.button == 4:
                        self.player.charge_attack()
                    if event.button == 11:
                        self.pause = True
                        self.movements = [False,False]  
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0 and "jump" in self.buffer:
                        self.buffer=[]
                        pass
                    if event.button == 7 and "dash" in self.buffer:
                        self.buffer=[]
                        pass
                    if event.button == 3 and "attack" in self.buffer:
                        self.buffer=[]
                        pass

            if self.buffer:
                self.buffer[1] -= 1
                if self.buffer[1] == 0:
                    self.buffer=[]
                elif self.buffer[0] == "jump":
                    if self.player.jump():
                        self.buffer=[]
                elif self.buffer[0] == "dash":
                    if self.player.dash():
                        self.buffer=[]
                elif self.buffer[0] == "attack":
                    if self.player.attack():
                        self.buffer=[]
                    

 

            self.screen_shake_timer = max(0,self.screen_shake_timer-1)
            self.screen_shake_offset = [random.randint(-self.screen_shake_timer,self.screen_shake_timer),random.randint(-self.screen_shake_timer,self.screen_shake_timer)]  


            #redering HP acording to player's HP
            for i in range(self.player.HP):
                self.display_for_outline.blit(self.assets['HP'],(i*18,15))
            #rendering boss HP, scale the horizontal to 58
            for enemy in self.enemy_spawners:
                if enemy.phase != 3 and enemy.HP < enemy.max_HP:
                    ratio = enemy.HP/enemy.max_HP
                    pygame.draw.rect(self.display_for_outline,(255,0,0),(233+55*(1-ratio),34,55*ratio,4))
                    self.display_for_outline.blit(pygame.transform.scale(self.assets['Boss_empty'],(58,12)),(230,30))
                elif enemy.phase == 3 and enemy.timer_HP < enemy.max_HP:
                    ratio = enemy.timer_HP/enemy.max_HP
                    #orange
                    pygame.draw.rect(self.display_for_outline,(255,127,0),(233+55*(1-ratio),34,55*ratio,4))
                    self.display_for_outline.blit(pygame.transform.scale(self.assets['Boss_empty'],(58,12)),(230,30))
                else:
                    self.display_for_outline.blit(pygame.transform.scale(self.assets['Boss_full'],(58,12)),(230,30))
            
                
                      
            self.display_for_outline.blit(self.display, (0,0))
            self.screen.blit(pygame.transform.scale(self.display_for_outline, (2*SCREEN_Width, 2*SCREEN_HEIGHT)), self.screen_shake_offset) 
            #blit self.display_entity to screen without scaling
            if not self.dead:
                self.player.render_new(self.screen,offset=self.render_camera) #render player

            if self.transition:
                tran_surf=pygame.Surface(self.display.get_size())
                pygame.draw.circle(tran_surf,(255,255,255),(self.display.get_width()//4,self.display.get_height()//4),(30-abs(self.transition))*8)
                tran_surf.set_colorkey((255,255,255))
                self.display.blit(tran_surf,(0,0)) 
                self.screen.blit(pygame.transform.scale(self.display, (2*SCREEN_Width, 2*SCREEN_HEIGHT)), (0,0)) 


            if self.pause:
                #pause screen: blit a half transparent black screen
                pause_screen = pygame.Surface((SCREEN_Width, SCREEN_HEIGHT), pygame.SRCALPHA)
                pause_screen.fill((0, 0, 0, 128))  # RGBA: (0, 0, 0, 128) for half transparency
                self.screen.blit(pause_screen, (0, 0))
                self.pause_select = 0
                pygame.mixer.music.set_volume(0.1)

            
            pygame.display.update()
            self.clock.tick(FPS)

    def first_phase_cutscene(self):
        pass

main_game().run()
