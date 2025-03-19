# main.py

import pygame
import pygame_gui
import os
from settings import WIDTH, HEIGHT, ICON_PATH, BACKGROUND_PATH, IMAGE_FOLDER, PLAYER_PATH
from sprites import FallingSprite, PlayerSprite
from utils import load_font, display_game_over

def show_welcome_screen(manager):
    """
    Создает всплывающее окно с приветственным сообщением и кнопкой "Начать".

    :param manager: Менеджер pygame_gui.
    :return: Окно и кнопка.
    """
    window_rect = pygame.Rect(0, 0, 600, 300)
    window_rect.center = (WIDTH // 2, HEIGHT // 2)
    welcome_window = pygame_gui.elements.UIWindow(
        rect=window_rect,
        manager=manager,
        window_display_title="Путь в BackEnd разработку!",
    )

    # Текст приветствия
    text_rect = pygame.Rect(50, 50, 500, 100)
    welcome_text = pygame_gui.elements.UITextBox(
        html_text="Добро пожаловать в игру про мой путь к BackEnd разработчику!",
        relative_rect=text_rect,
        manager=manager,
        container=welcome_window,
    )

    # Кнопка "Начать"
    button_rect = pygame.Rect(200, 180, 200, 50)
    start_button = pygame_gui.elements.UIButton(
        relative_rect=button_rect,
        text="Начать",
        manager=manager,
        container=welcome_window,
    )

    return welcome_window, start_button

def main():
    """
    Основная функция, которая запускает игру.
    """
    pygame.init()

    # Настройка экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Путь в BackEnd разработку")
    pygame.display.set_icon(pygame.image.load(ICON_PATH))

    # Менеджер pygame_gui
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))

    # Показ приветственного окна
    welcome_window, start_button = show_welcome_screen(manager)

    # Загрузка фонового изображения
    background = pygame.image.load(BACKGROUND_PATH)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Загрузка шрифта
    font = load_font()

    # Создание спрайтов
    image_files = [os.path.join(IMAGE_FOLDER, img) for img in os.listdir(IMAGE_FOLDER) if img.endswith(('.png', '.jpg', '.jpeg'))]
    falling_sprites = pygame.sprite.Group()
    for img_path in image_files:
        for _ in range(2):
            sprite = FallingSprite(img_path)
            falling_sprites.add(sprite)

    player_sprite = PlayerSprite(PLAYER_PATH)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(falling_sprites)
    all_sprites.add(player_sprite)

    # Счетчик очков
    score = 0
    score_timer = 0

    # Игровой цикл
    clock = pygame.time.Clock()
    run = True
    game_over = False
    game_started = False  # Флаг начала игры
    while run:
        time_delta = clock.tick(30) / 1000.0  # Время, прошедшее с последнего кадра

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Обработка событий pygame_gui
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    game_started = True  # Начинаем игру
                    welcome_window.kill()  # Закрываем приветственное окно

            manager.process_events(event)

        if game_started and not game_over:
            # Обновление спрайтов
            all_sprites.update()

            # Увеличение очков
            score_timer += clock.get_time()
            if score_timer >= 1000:
                score += 1
                score_timer = 0

            # Проверка столкновений
            if pygame.sprite.spritecollideany(player_sprite, falling_sprites):
                game_over = True

        # Отрисовка
        screen.blit(background, (0, 0))
        if game_started:
            if not game_over:
                all_sprites.draw(screen)
                score_text = font.render(f"Очки: {score}", True, (255, 0, 0))
                screen.blit(score_text, (10, 10))
            else:
                display_game_over(screen, font, score)

        # Обновление pygame_gui
        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()