import pygame


class Player(pygame.sprite.Sprite): # herite de la super classe sprite (element graphique)

    def __init__(self, x, y): # initialisation
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png') # recupere l'image du joueur
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0]) #enlève le fond noir autour du joueur
        self.rect = self.image.get_rect() #definir sa position (c'est un rectangle)
        self.position = [x, y]
        self.speed = 1 #constante vitesse de deplacement

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32)) # extraire un morceau de l'image
        return image