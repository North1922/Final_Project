# utils.py

import pygame
from settings import WIDTH, HEIGHT, FONT_SIZE, END_SCREEN_PATH

def load_font():
    """
    Загружает шрифт для отображения текста.

    :return: Объект шрифта.
    """
    return pygame.font.Font(None, FONT_SIZE)

def display_game_over(screen, font, score):
    """
    Отображает экран завершения игры с изображением и итоговыми очками.

    :param screen: Экран Pygame.
    :param font: Шрифт для отображения текста.
    :param score: Количество очков.
    """
    # Загрузка изображения завершения игры
    end_image = pygame.image.load(END_SCREEN_PATH)
    screen.blit(end_image, (WIDTH // 2 - end_image.get_width() // 2, HEIGHT // 2 - end_image.get_height() // 2))

    # Отображение итоговых очков
    final_score_text = font.render(f"Итоговые очки: {score}", True, (255, 0, 0))
    screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 127))