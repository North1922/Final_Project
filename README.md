# Игра: Мой путь к BackEnd разработчику
**Эта игра была создана в рамках финального проекта к бесплатному курсу по базовому Python от Максима WOZBORN (https://github.com/WOZBORN, https://www.twitch.tv/wozborn)**
Игра олицетвояряет мой путь к BackEnd разработчику. Что же свалится на голову к человеку который начинает изучать BackEnd?

Строго прошу не судить, чего-то сложного и сверх умного здесь вы не найдёте, но думаю улыбнётесь) В рамках бесплатного курса был присутствовал некий челендж,
первые три человека которые выполнят все домашние задание и два проекта(промежуточный и финальный) попадут на платное обучение Python BackEnd к https://github.com/WOZBORN.

По мимо большого колличества информации , сложнорсть заключалась в разных часовых поясах. Стримы по Московскому времени заканчивались достаточно поздно , а ещё нужно было успеть
сдать дз до начала следующего урока(Уроки были каждый день за исключением субботы и воскресенья). Пришлось жертвовать сном и хорошим самочувтсвием, но как итог финальный проект сдал первым.


- **Управление**: Игрок управляет спрайтом с помощью клавиш ← и →.
- **Падающие объекты**: Сверху падают случайные объекты, которых нужно избегать.
- **Счетчик очков**: За каждую секунду игры начисляется 1 очко.
- **Завершение игры**: При столкновении с падающим объектом игра завершается, и на экране отображается итоговое количество очков.
- **Приветственное окно**: При запуске игры появляется окно с приветствием и кнопкой "Начать".

---

## Установка и запуск

### Требования

- Python 3.7 или выше
- Библиотека Pygame
- Библиотека pygame_gui

### Установка зависимостей

1. Установите Python с официального сайта: [python.org](https://www.python.org/).
2. Установите необходимые библиотеки:

  ``` pip install pygame pygame_gui```

## Запуск игры
### Клонируйте репозиторий:
```git clone https://github.com/North1922/Final_Project```
### Запустите игру:
```cd ваш-репозиторий```
```python main.py```

## Структура проекта
- main.py: Основной файл, запускающий игру.

- settings.py: Содержит константы и настройки игры.

- sprites.py: Содержит классы спрайтов (игрок и падающие объекты).

- utils.py: Вспомогательные функции для отображения текста и завершения игры.

- images/: Папка с изображениями для игры.
  - player/: Изображения, связанные с игроком.
  - north.png: Главный спрайт игрока.
  - back_fone.jpg: Фоновое изображение.
  - The_end.png: Изображение для завершающего экрана.

  ## Как играть
- 1.Запустите игру.

- 2.Нажмите кнопку "Начать" в приветственном окне.

- 3.Управляйте спрайтом с помощью клавиш ← и →.

- 4.Уклоняйтесь от падающих объектов.

- 5.Набирайте очки, стараясь продержаться как можно дольше.

## Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

## Автор
North1922
