import pygame

def display_menu():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Choix des pics et disques - Tour de Hanoï")
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 28)

    pegs_text = ""
    disks_text = ""
    selected_gamemode = None
    create_mode = False
    peg_mode = True
    disk_mode = False

    pegs_box = pygame.Rect(200, 100, 200, 40)
    disks_box = pygame.Rect(200, 200, 200, 40)
    play_button = pygame.Rect((600 - 150) // 2, 300, 150, 45) 

    running = True
    while running:
        screen.fill((30, 30, 30))

        title = font.render("Sélection ou création de joueur", True, (255, 255, 255))
        screen.blit(title, (100, 30))

        pygame.draw.rect(screen, (255, 255, 255), pegs_box, 2)
        input_surface_1 = font.render(pegs_text, True, (255, 255, 255))
        screen.blit(input_surface_1, (pegs_box.x + 10, pegs_box.y + 5))

        pegs_label = label_font.render("pegs", True, (200, 200, 200))
        screen.blit(pegs_label, (pegs_box.x - 60, pegs_box.y + 8))

        pygame.draw.rect(screen, (255, 255, 255), disks_box, 2)
        input_surface_2 = font.render(disks_text, True, (255, 255, 255))
        screen.blit(input_surface_2, (disks_box.x + 10, disks_box.y + 5))

        disks_label = label_font.render("disk", True, (200, 200, 200))
        screen.blit(disks_label, (disks_box.x - 60, disks_box.y + 8))

        pygame.draw.rect(screen, (0, 128, 0), play_button)
        screen.blit(font.render("Jouer", True, (255, 255, 255)), (play_button.x + 30, play_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            elif event.type == pygame.KEYDOWN:
                if peg_mode and create_mode:
                    if event.key == pygame.K_RETURN and pegs_text.strip() and disks_text.strip():
                        disks = int(disks_text.strip())
                        pegs = int(pegs_text.strip())
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        pegs_text = pegs_text[:-1]
                    else:
                        pegs_text += event.unicode

                elif disk_mode and create_mode:
                    if event.key == pygame.K_RETURN and pegs_text.strip() and disks_text.strip():
                        disks = int(disks_text.strip())
                        pegs = int(pegs_text.strip())
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        disks_text = disks_text[:-1]
                    else:
                        disks_text += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pegs_box.collidepoint(event.pos):
                    create_mode = True
                    peg_mode = True
                    disk_mode = False

                elif disks_box.collidepoint(event.pos):
                    create_mode = True
                    peg_mode = False
                    disk_mode = True

                elif play_button.collidepoint(event.pos):
                    if pegs_text.strip() and disks_text.strip():
                        pegs = int(pegs_text.strip())
                        disks = int(disks_text.strip())
                        selected_gamemode = (pegs, disks)
                        running = False

    return selected_gamemode