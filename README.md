# Работа с Bitly

Программа создана для перевода длинных ссылок в битлинки или для подсчета количества кликов по битлинку.

## Перед началом работы
1. Необходимо получить `GENERIC ACCESS TOKEN`. Для этого:

    1.1. Зарегистрируйтесь на сайте [Bitly](https://bit.ly).

    1.2. Затем получите свой уникальный `GENERIC ACCESS TOKEN`, 
    зайдя в раздел `PROFILE SETTINGS`, 
    далее в раздел `GENERIC ACCESS TOKEN`.

2. Необходимо передать токен в main.py. Для этого:

    2.1. В каталоге проекта создайте пустой файл .env.

    2.2. В файл .env запишите `GENERIC ACCESS TOKEN` в следующем формате:

    ```
    BITLY_TOKEN=Bearer Ваш_GENERIC_ACCESS_TOKEN
    ```
3. Требуется создать виртуальное окружения и активировать его.
Для этого следуйте следующим указаниям:

    3.1. Создайте новое виртуальное окружение, запустив в терминале следующую команду:

    ```bash
    python3 -m venv название_виртуального_окружения /полный/путь/до/папки/виртуального/окружения
    ```

    3.2. Теперь необходимо активировать виртуальное окружение, для этого выполните следующую команду:

    ```bash
    source /полный/путь/до/папки/виртуального/окружения/bin/activate
    ```
    
    При желании получить больше информации или 
    использовать другие средства для создания виртуального окружения,
    можете ознакомиться со следующими ресурсами:
    
    [Что такое виртуальное окружение](https://devman.org/qna/12/chto-takoe-virtualnoe/)
    
    [Виртуальное окружение](https://devman.org/encyclopedia/pip/pip_virtualenv/)
    
    [Requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
    
4. Необходимо загрузить в виртуальное окружение библиотеки из файла requirements.txt. 
Для этого, уже активировав виртуальное окружение, выполните следующую команду:

    ```bash
    pip install -r requirements.txt
    ```
    
## Запуск программы

У программы есть два варианта работы. 

1. Программа сокращает длинные ссылки до битлинков. 
Для успешного выполнения данной задачи введите в терминале следующую команду:

```bash
python3 main.py https://dvmn.org/modules/
```
, где https://dvmn.org/modules/ - ссылка, которую требуется сократить.

Пример результата выполнения вышеуказанной команды:

```bash
Битлинк bit.ly/3mop9Ev.
```

2. Программа возвращает количество кликов на битлинк.
Для успешного выполнения данной задачи введите в терминале следующую команду:

```bash
python3 main.py bit.ly/3mop9Ev
```
,где bit.ly/3mop9Ev - битлинк, для которого требуется получить количество кликов.

Пример результата выполнения вышеуказанной команды:

```bash
Было совершено следующее количество кликов: 2.
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).


