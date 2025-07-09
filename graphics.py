# graphics.py

import pygame
from solve import HanoiSolver

class HanoiGame:
    def __init__(self, disks):
        pygame.init()
        pygame.mixer.init()

        self.disks = disks
        self.pegs = [[], [], []]
        self.init_disks()

        self.screen_width = 800
        self.screen_height = 600
        self.disk_height = 20
        self.peg_width = 10

        self.peg_positions = [
            self.screen_width // 4,
            self.screen_width // 2,
            3 * self.screen_width // 4
        ]

        self.disk_colors = [
            (255, 0, 0), (255, 165, 0), (255, 255, 0),
            (0, 128, 0), (0, 255, 255), (0, 0, 255),
            (128, 0, 128), (255, 192, 203), (160, 82, 45)
        ]

        self.selected_peg = 0      # pique sélectionnée
        self.holding_disk = None   # disque en cours de déplacement

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tour de Hanoï")

        self.clock = pygame.time.Clock()
        self.running = True

        try:
            self.move_sound = pygame.mixer.Sound("assets/move.mp3")
        except pygame.error:
            self.move_sound = None
            print("⚠️ move.mp3 introuvable, pas de son.")

        
        self.solve_button_rect = pygame.Rect(self.screen_width - 120, 20, 100, 40)
        self.quit_button_rect = pygame.Rect(self.screen_width - 120, 70, 100, 40)

    def draw_solve_button(self):
        pygame.draw.rect(self.screen, (70, 130, 180), self.solve_button_rect, border_radius=8)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Solve", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.solve_button_rect.center)
        self.screen.blit(text, text_rect)
    
    def draw_quit_button(self):
        pygame.draw.rect(self.screen, (180, 70, 70), self.quit_button_rect, border_radius=8)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Quit", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.quit_button_rect.center)
        self.screen.blit(text, text_rect)

    def init_disks(self):
        self.pegs = [[], [], []]
        for i in range(self.disks, 0, -1):
            self.pegs[0].append(i)

    def draw_table_and_pegs(self):
        # Table
        pygame.draw.rect(self.screen, (100, 50, 20), (0, self.screen_height - 40, self.screen_width, 40))

        # Piques
        for i, x in enumerate(self.peg_positions):
            color = (255, 255, 0) if i == self.selected_peg else (200, 200, 200)
            pygame.draw.rect(self.screen, color, (x - self.peg_width // 2, 200, self.peg_width, 200))

    def draw_disks(self):
        for peg_index, peg in enumerate(self.pegs):
            x_center = self.peg_positions[peg_index]
            for disk_index, disk_size in enumerate(peg):
                width = 40 + disk_size * 15
                height = self.disk_height
                x = x_center - width // 2
                y = self.screen_height - 50 - disk_index * height
                color = self.disk_colors[(disk_size - 1) % len(self.disk_colors)]
                pygame.draw.rect(self.screen, color, (x, y, width, height), border_radius=6)

        # Affichage du disque "en main"
        if self.holding_disk is not None:
            width = 40 + self.holding_disk * 15
            height = self.disk_height
            x_center = self.peg_positions[self.selected_peg]
            x = x_center - width // 2
            y = 150
            color = self.disk_colors[(self.holding_disk - 1) % len(self.disk_colors)]
            pygame.draw.rect(self.screen, color, (x, y, width, height), border_radius=6)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.draw_table_and_pegs()
        self.draw_disks()
        self.draw_solve_button()
        self.draw_quit_button()
        pygame.display.flip()

    def move_selection(self, direction):
        self.selected_peg = (self.selected_peg + direction) % 3

    def handle_enter(self):
        peg = self.pegs[self.selected_peg]
        if self.holding_disk is None:
            if peg:
                self.holding_disk = peg.pop()
                if self.move_sound: self.move_sound.play()
        else:
            if not peg or peg[-1] > self.holding_disk:
                peg.append(self.holding_disk)
                self.holding_disk = None
                if self.move_sound: self.move_sound.play()

    def reset(self):
        self.init_disks()
        self.holding_disk = None
        self.selected_peg = 0

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_selection(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.move_selection(1)
                    elif event.key == pygame.K_RETURN:
                        self.handle_enter()
                    elif event.key == pygame.K_r:
                        self.reset()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.solve_button_rect.collidepoint(event.pos):
                        print("Solve button clicked (fonction à implémenter)")
                    elif self.quit_button_rect.collidepoint(event.pos):
                        self.running = False


        pygame.quit()
