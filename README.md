# Ring Fantasy

Это 2D RPG-игра. Вы играете за персонажа, попавшего в неизведанный мир. Вам придется сражаться с монстрами, 
добывать снаряжение и выполнять поручения.

## ВНИМАНИЕ!!! Это альфа-версия. Игра в разработке.
На данный момент доступен только один уровень.

![Внешний вид](images/screen.png)

### Запуск игры
Игра написана на языке Python с использованием библиотеки Pygame. 
Для запуска игры потребуется установленный Python (желательно версии 3.10).

Склонировать проект и перейти в него:
```
git clone https://github.com/dmitrii-r/ring_fantasy
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить игру:
```
python ring_fantasy.py
```

### Управление.
- стрелки UP, DOWN, LEFT, RIGHT - управление движением персонажа;
- клавиша P - меню персонажа;
- мышь - остальные действия;
