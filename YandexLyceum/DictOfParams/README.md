# Словарь из параметров

Используя sys.argv напишите программу, которая разбирает аргументы командной строки вида "ключ=значение"и выводит их на отдельной строке в виде "Key: ключ Value: значение".
Кроме описанных аргументов программа может принимать необязательную опцию --sort, которая позволяет отсортировать выводимые значения по ключу.

## Пример 1
```python
# Ввод
python3 solution.py --sort name=Vasya age=42
```
```python
# Вывод
Key: age Value: 42
Key: name Value: Vasya
```
## Пример 2
```python
# Ввод
python3 solution.py --sort surname=Ivanov name=Vasya age=42
```
```python
# Вывод
Key: age Value: 42
Key: name Value: Vasya
Key: surname Value: Ivanov
```