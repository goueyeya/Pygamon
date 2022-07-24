import pygame
import pytmx
import pyscroll

from Player import Player


class Game:

    def __init__(self):  # fonction qui se fait au load du jeu
        # fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600))  # set la taille de la fenetre
        pygame.display.set_caption("Pygamon")  # set le nom de la fenêtre

        # charger la carte tmx
        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")  # specifier le fichier qui contient la carte
        map_data = pyscroll.data.TiledMapData(tmx_data)  # recuperer les donnéees de cette carte
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())  # assembler les calques
        map_layer.zoom = 2

        #generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player) # dessine le joueur

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] or pressed[pygame.K_z] :
            self.player.move_up()
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.player.move_right()

    def run(self):
        # boucle infini du jeu
        clock = pygame.time.Clock()

        running = True  # bolean a true quand le jeu tourne
        while running:

            self.handle_input()#gere les inputs pour contoler le joueur
            self.group.update()
            self.group.center(self.player.rect.center) #centre la "camera" sur le joueur
            self.group.draw(self.screen)  # dessiner les calques sur le screen
            pygame.display.flip()  # actualisation de la carte en temps reel
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(144)

        # exctinction du jeu
        pygame.quit()
