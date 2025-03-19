# settings.py

import os

# Размеры экрана
WIDTH = 1800
HEIGHT = 900

# Размеры спрайтов
SPRITE_SIZE = (100, 100)  # Размер падающих спрайтов
MAIN_SPRITE_SIZE = (100, 150)  # Размер главного спрайта

# Шрифт
FONT_SIZE = 50  # Размер шрифта для отображения очков

# Пути к изображениям
IMAGE_FOLDER = "images"
PLAYER_FOLDER = os.path.join(IMAGE_FOLDER, "player")
ICON_PATH = os.path.join(IMAGE_FOLDER, "git_cat.png")
BACKGROUND_PATH = os.path.join(PLAYER_FOLDER, "back_fone.jpg")
PLAYER_PATH = os.path.join(PLAYER_FOLDER, "north.png")
END_SCREEN_PATH = os.path.join(PLAYER_FOLDER, "The_end.png")