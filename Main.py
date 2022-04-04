#
# Created following these tutorials: https://youtu.be/FObLawDOLBc
# You are at the point in the link above.
#

import pygame, sys
from Sounds import *
from Player import *
from MapBuild import *
import Maps
from Sprites import *
from Config import *

pygame.display.set_caption("")

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.terrainsheet = Spritesheet('res/ground.png')
        self.character_spritesheet = Spritesheet('res/character.png')
        self.enemy_spritesheet = Spritesheet('res/enemy.png')
        self.attack_spritesheet = Spritesheet('res/attack.png')

    def createTilemap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.trees = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap(tilemap)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == "up":
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill('Black')
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


TILEMAP = Maps.world_1.stage_1
game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()
