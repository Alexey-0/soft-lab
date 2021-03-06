### Команда ls

### Описание
##### Отображает исчерпывающую информацию о файлах и каталогах. На пример, может показать права доступа, отобразить скрытые файлы, сортировать вывод и тд.

### Синтаксис
##### ls [OPTIONS] [PATH]

### Популярные опции

Опция | Назначение
------|----
-a | Отображает все файлы, в том числе и скрытые
-l | Показывает подробную информацию о файлах (права, владелец, время последнего изменения)
-R | Рекурсивное отображение (оображает содежрымое поддерикторий)
-t | Сортирует вывод по времени создания или последнего изменения файлоф, от новых к старым
-S | Сортировка по размеру файлов, от большего к меньшему
-r | обратный порядок сотрировки
-sh| выводить размер файла

### Примеры
#### Показать содержимое директории /var/log/
 ![image](https://user-images.githubusercontent.com/82635801/163769200-ff027315-47a0-4c55-af08-d3414d17d31a.png)
#### Показать содержимое текущей директории
 ![image](https://user-images.githubusercontent.com/82635801/163768917-d4539e25-6b09-44e5-8c4c-e515861ec74f.png)
#### Отображение скрытых файлов в текущей директории
 ![image](https://user-images.githubusercontent.com/82635801/163769797-5dc0371d-3aa0-471c-9db0-cab59a3b60c6.png)
> Пояснение: файлы начинающеся с точки - скрытые
#### Показать подробную информацию
 ![image](https://user-images.githubusercontent.com/82635801/163769964-38d58407-42af-4fa0-b026-9969d9e46a5e.png)
####  Рекурсивное отображение начиная с каталога /var/spool/
 ![image](https://user-images.githubusercontent.com/82635801/163770973-03198e62-0ba7-4939-a6f4-3f7bab54972f.png)
> Пояснение: в каталоге /var/spool/ нашлость 2 директории (cron и rsyslog) и 1 ссылка, в /var/spool/cron/ есть ещё 3 директории, они пустые, в /var/spool/rsyslog тоже пусто
#### Отсортировать по размеру каталог /etc/ (-S) и показать размер файлов и катологов (-sh)
![image](https://user-images.githubusercontent.com/82635801/163773605-d9aee44d-fc4c-4239-97d9-96ac3f1b25c6.png)
#### Отсортировать по последниму изменению файла содержимое каталога /etc/ и вывести подробную информацию
![image](https://user-images.githubusercontent.com/82635801/163775023-a0fa6b1d-7bd9-45ec-bcfb-a16aeb2b17bc.png)

<br>

Команда cd
====

### Описание
##### Позволяет менять рабочию директорию

### Синтаксис
##### cd [OPTIONS] [PATH] 

> Есть несколько опций но они пактически  бесполезны.

### Примеры
##### Смнена рабочего каталога
![image](https://user-images.githubusercontent.com/82635801/163777599-31d5461e-da04-4bf5-8215-ec383b38a660.png)
> Так же можно использовать и отностительный путь
##### Быстрый переход в домашний каталог
![image](https://user-images.githubusercontent.com/82635801/163776923-e5e995dc-6550-4c0f-8234-6a887b358ebf.png)



