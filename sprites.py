# sprites.py

import pygame
import random
from settings import WIDTH, HEIGHT, SPRITE_SIZE, MAIN_SPRITE_SIZE

class FallingSprite(pygame.sprite.Sprite):
    """
    Класс для падающих спрайтов.
    Спрайты двигаются сверху вниз с случайной скоростью и задержкой.
    """
    def __init__(self, image_path):
        """
        Инициализация падающего спрайта.

        :param image_path: Путь к изображению спрайта.
        """
        super().__init__()
        self.original_image = pygame.image.load(image_path)  # Загрузка картинки
        self.image = pygame.transform.scale(self.original_image, SPRITE_SIZE)  # Изменение размера
        self.rect = self.image.get_rect()  # Создание рамки
        self.rect.x = random.randint(0, WIDTH - self.rect.width)  # Случайная начальная позиция по X
        self.rect.y = random.randint(-HEIGHT, -self.rect.height)  # Случайная начальная позиция по Y
        self.speed = random.randint(3, 10)  # Случайная скорость падения
        self.delay = random.randint(0, 60)  # Случайная задержка перед началом падения

    def update(self):
        """
        Обновление позиции спрайта.
        Если задержка закончилась, спрайт начинает падать.
        """
        if self.delay > 0:
            self.delay -= 1  # Уменьшаем задержку
        else:
            # Движение спрайта по вертикали сверху вниз
            self.rect.y += self.speed
            if self.rect.y > HEIGHT:  # Если спрайт уходит за нижнюю границу экрана
                self.reset()  # Перемещаем его обратно наверх

    def reset(self):
        """
        Сбрасывает спрайт наверх с новыми случайными параметрами.
        """
        self.rect.x = random.randint(0, WIDTH - self.rect.width)  # Случайная позиция по X
        self.rect.y = random.randint(-HEIGHT, -self.rect.height)  # Случайная позиция по Y
        self.speed = random.randint(3, 10)  # Новая случайная скорость
        self.delay = random.randint(0, 60)  # Новая случайная задержка


class PlayerSprite(pygame.sprite.Sprite):
    """
    Класс для главного спрайта (игрока).
    Игрок двигается только по горизонтали в нижней части экрана.
    """
    def __init__(self, image_path):
        """
        Инициализация главного спрайта.

        :param image_path: Путь к изображению спрайта.
        """
        super().__init__()
        self.original_image = pygame.image.load(image_path)  # Загрузка картинки
        self.image = pygame.transform.scale(self.original_image, MAIN_SPRITE_SIZE)  # Изменение размера
        self.rect = self.image.get_rect()  # Создание рамки
        self.rect.x = WIDTH // 2 - self.rect.width // 2  # Начальная позиция по X (центр экрана)
        self.rect.y = HEIGHT - self.rect.height - 20  # Позиция по Y (внизу экрана с отступом 20px)
        self.speed = 10  # Скорость движения

    def update(self):
        """
        Обновление позиции главного спрайта.
        Управление движением с помощью клавиш LEFT и RIGHT.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:  # Движение влево
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:  # Движение вправо
            self.rect.x += self.speed