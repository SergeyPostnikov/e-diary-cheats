# cheatings.py
модуль с тремя функциями для редактирования базы данных проекта [e-diary](https://github.com/devmanorg/e-diary) 
### get_schoolkid - получаем ученика
функция принимает имя ученика и возврашает объект типа Schooolkid

### fix_marks - исправляем оценки
функция принимает объект типа Schooolkid и заменяет оценки 2 и 3 на 5 в дневнике.

### remove_chastisements - удаляем замечания
функция принимает объект типа Schooolkid и удвляет замечания в дневнике.

### create_commendation
функция принимает имя ученика и название предмета  
создавая похвалу 'Хвалю!' в дненвнике для последнего урока 
по этому предмету.

## Использвание
поместить файл cheatings.py в папку с manage.py и вызвать:
```
python3 manage.py shell
```
затем в интерактивном режиме можно ввести
```
from cheatings import *
me = get_schoolkid('Пётр Петров')                    # получаем запись из бд по ***вашему*** имени
fix_marks(me)                                        # исправляем оценки
remove_chastisements(me)                             # убираем замечания
create_commendation('Пётр Петров', 'Математика')     # создаём похвалу по вашему имени и предмету
```
