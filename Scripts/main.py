import pygame
import sys

pygame.init()

# -----------------------------
# WINDOW
# -----------------------------
WIDTH = 1000
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChronoCash - Time Is Money")

clock = pygame.time.Clock()

# -----------------------------
# COLORS
# -----------------------------
BG = (20, 22, 30)
WHITE = (240, 240, 240)
RED = (220, 70, 70)
GREEN = (70, 200, 110)
YELLOW = (240, 190, 60)
BLUE = (80, 150, 230)
GRAY = (60, 65, 80)
DARK = (35, 38, 50)
HOVER = (255, 255, 255)

# -----------------------------
# FONTS
# -----------------------------
title_font = pygame.font.Font(None, 72)
big_font = pygame.font.Font(None, 48)
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

# -----------------------------
# GAME VARIABLES
# -----------------------------
max_time = 60
time_left = 60.0
money = 0
job_level = 1

game_started = False
game_over = False

survival_time = 0.0
best_survival = 0.0

message = "Survive as long as possible!"
message_timer = 3

# -----------------------------
# BUTTONS
# -----------------------------
start_button = pygame.Rect(350, 390, 300, 75)

work_button = pygame.Rect(100, 300, 220, 80)
coffee_button = pygame.Rect(390, 300, 220, 80)
medicine_button = pygame.Rect(680, 300, 220, 80)

upgrade_button = pygame.Rect(100, 420, 800, 70)

restart_button = pygame.Rect(350, 500, 300, 70)


# -----------------------------
# FUNCTIONS
# -----------------------------
def draw_text(text, font_type, color, x, y, center=False):
    surface = font_type.render(text, True, color)

    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)


def draw_button(rect, text, color):
    mouse = pygame.mouse.get_pos()

    button_color = color

    # Hover effect
    if rect.collidepoint(mouse):
        button_color = tuple(min(c + 25, 255) for c in color)

    pygame.draw.rect(
        screen,
        button_color,
        rect,
        border_radius=12
    )

    draw_text(
        text,
        font,
        WHITE,
        rect.centerx,
        rect.centery,
        center=True
    )


def reset_game():
    global time_left
    global money
    global job_level
    global game_over
    global game_started
    global survival_time
    global message
    global message_timer

    time_left = 60
    money = 0
    job_level = 1

    game_over = False
    game_started = True

    survival_time = 0

    message = "Survive as long as possible!"
    message_timer = 3


def show_message(text):
    global message
    global message_timer

    message = text
    message_timer = 2


def end_game():
    global game_over
    global best_survival

    game_over = True

    if survival_time > best_survival:
        best_survival = survival_time


# -----------------------------
# MAIN LOOP
# -----------------------------
running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse = pygame.mouse.get_pos()

            # -----------------------------
            # START SCREEN
            # -----------------------------
            if not game_started:

                if start_button.collidepoint(mouse):
                    reset_game()

            # -----------------------------
            # GAMEPLAY
            # -----------------------------
            elif not game_over:

                # WORK
                if work_button.collidepoint(mouse):

                    earnings = 10 * job_level
                    time_cost = 5

                    money += earnings
                    time_left -= time_cost

                    show_message(
                        f"Worked! +${earnings}  -{time_cost}s"
                    )

                    if time_left <= 0:
                        time_left = 0
                        end_game()

                # COFFEE
                elif coffee_button.collidepoint(mouse):

                    cost = 15

                    if money >= cost:

                        money -= cost
                        time_left += 5

                        if time_left > max_time:
                            time_left = max_time

                        show_message(
                            "Coffee bought! +5 seconds"
                        )

                    else:
                        show_message(
                            "Not enough money!"
                        )

                # MEDICINE
                elif medicine_button.collidepoint(mouse):

                    cost = 30

                    if money >= cost:

                        money -= cost
                        time_left += 12

                        if time_left > max_time:
                            time_left = max_time

                        show_message(
                            "Medicine! +12 seconds"
                        )

                    else:
                        show_message(
                            "Not enough money!"
                        )

                # UPGRADE
                elif upgrade_button.collidepoint(mouse):

                    cost = 50

                    if money >= cost:

                        money -= cost
                        job_level += 1

                        show_message(
                            f"Promotion! Job Level {job_level}"
                        )

                    else:
                        show_message(
                            "Need $50 for promotion!"
                        )

            # -----------------------------
            # GAME OVER
            # -----------------------------
            else:

                if restart_button.collidepoint(mouse):
                    reset_game()

    # -----------------------------
    # TIME DRAIN
    # -----------------------------
    if game_started and not game_over:

        time_left -= dt
        survival_time += dt

        if time_left <= 0:

            time_left = 0
            end_game()

    # -----------------------------
    # DRAW BACKGROUND
    # -----------------------------
    screen.fill(BG)

    # =========================================================
    # START SCREEN
    # =========================================================
    if not game_started:

        draw_text(
            "CHRONOCASH",
            title_font,
            WHITE,
            WIDTH // 2,
            150,
            center=True
        )

        draw_text(
            "TIME IS MONEY",
            big_font,
            YELLOW,
            WIDTH // 2,
            220,
            center=True
        )

        draw_text(
            "Every second of your life has value.",
            font,
            WHITE,
            WIDTH // 2,
            285,
            center=True
        )

        draw_text(
            "Work to earn money. Spend money to buy time.",
            small_font,
            GRAY,
            WIDTH // 2,
            320,
            center=True
        )

        draw_button(
            start_button,
            "START GAME",
            BLUE
        )

        draw_text(
            "Survive as long as possible.",
            small_font,
            WHITE,
            WIDTH // 2,
            500,
            center=True
        )

    # =========================================================
    # GAMEPLAY SCREEN
    # =========================================================
    elif not game_over:

        # TITLE
        draw_text(
            "CHRONOCASH",
            title_font,
            WHITE,
            WIDTH // 2,
            50,
            center=True
        )

        draw_text(
            "TIME IS MONEY",
            font,
            YELLOW,
            WIDTH // 2,
            95,
            center=True
        )

        # TIME
        draw_text(
            f"TIME: {int(time_left)}s",
            big_font,
            RED,
            80,
            145
        )

        pygame.draw.rect(
            screen,
            DARK,
            (80, 200, 840, 30),
            border_radius=10
        )

        bar_width = int(
            840 * (time_left / max_time)
        )

        pygame.draw.rect(
            screen,
            RED,
            (80, 200, bar_width, 30),
            border_radius=10
        )

        # MONEY
        draw_text(
            f"MONEY: ${money}",
            big_font,
            GREEN,
            650,
            140
        )

        draw_text(
            f"JOB LEVEL: {job_level}",
            font,
            BLUE,
            650,
            180
        )

        # SURVIVAL TIME
        draw_text(
            f"SURVIVED: {int(survival_time)}s",
            small_font,
            WHITE,
            80,
            245
        )

        # BUTTONS
        draw_button(
            work_button,
            f"WORK +${10 * job_level}",
            BLUE
        )

        draw_button(
            coffee_button,
            "COFFEE $15",
            GREEN
        )

        draw_button(
            medicine_button,
            "MEDICINE $30",
            RED
        )

        draw_button(
            upgrade_button,
            "UPGRADE JOB  -  $50",
            YELLOW
        )

        # MESSAGE
        if message_timer > 0:

            draw_text(
                message,
                font,
                WHITE,
                WIDTH // 2,
                550,
                center=True
            )

            message_timer -= dt

    # =========================================================
    # GAME OVER SCREEN
    # =========================================================
    else:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(235)
        overlay.fill((10, 10, 15))

        screen.blit(
            overlay,
            (0, 0)
        )

        draw_text(
            "TIME'S UP!",
            title_font,
            RED,
            WIDTH // 2,
            180,
            center=True
        )

        draw_text(
            f"Survival Time: {int(survival_time)} seconds",
            big_font,
            WHITE,
            WIDTH // 2,
            260,
            center=True
        )

        draw_text(
            f"Final Money: ${money}",
            font,
            GREEN,
            WIDTH // 2,
            315,
            center=True
        )

        draw_text(
            f"Final Job Level: {job_level}",
            font,
            BLUE,
            WIDTH // 2,
            355,
            center=True
        )

        draw_text(
            f"Best Survival: {int(best_survival)} seconds",
            font,
            YELLOW,
            WIDTH // 2,
            395,
            center=True
        )

        draw_button(
            restart_button,
            "PLAY AGAIN",
            BLUE
        )

    # -----------------------------
    # DISPLAY
    # -----------------------------
    pygame.display.flip()


pygame.quit()
sys.exit() 