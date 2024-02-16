# Интерактивная карта Москвы

Этот проект - интерактивная карта Москвы, где пользователи могут просматривать различные виды
активного отдыха с подробными описаниями и комментариями. 

Дополнительные функции - добавляются администратором вручную через специальный интерфейс.

## Установка при развертывании проекта локально

Для установки проекта, выполните следующие шаги:

1. Склонируйте репозиторий:
```bash
git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
```
2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv env
source env/bin/activate
```
Работоспособность проекта протестирована на python 3.10
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте файл .env и заполните в нем следующие переменные:
```
SECRET_KEY=<YOUR SECRET KEY>
DEBUG=True
ALLOWED_HOSTS = ['*']
```

**SECRET_KEY** - Секретный ключ для конкретной установки Django. Он используется для обеспечения cryptographic signing,
и должен быть установлен на уникальное значение. [Сгенерировать](https://djecrety.ir)

**DEBUG** - Булево значение, которое включает/выключает режим отладки. 
Подробнее по [ссылке](https://django.fun/ru/docs/django/4.0/ref/settings/#debug).

**ALLOWED_HOSTS** - Список строк, представляющих имена хостов/доменов, которые может обслуживать данный Django-сайт 
Подробнее по [ссылке](https://django.fun/docs/django/5.0/ref/settings/).

6. Заполнение базы данных тестовыми данными:
Можно брать по [ссылке](https://github.com/devmanorg/where-to-go-places/tree/master/places)
```
python3 manage.py load_place <http://адрес/файл.json>

Например
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json
```

## Использование (локально)

Для интерфейса администратора нужно создать суперпользователя. Для этого выполните команду:

```bash
python manage.py createsuperuser
```
Затем запустите сам сервер
```bash
python manage.py runserver
```
В браузере и перейдите по адресу http://localhost:8000/ для просмотра интерактивной карты Москвы.
Добавление или изменение локаций, происходит в режиме администратора по ссылке: http://localhost:8000/admin.

**Интерфейс администратора позволяет:**

1. Просмотреть список локаций и найти локацию по названию.
2. Перейти на страницу редактирования локации где можно обновить описание. Добавить новые картинки или удалить старые, а также переместить их в начало списка, чтобы изменить порядок их отображения на сайте.
3. Добавить новые локации или удалить старые

## Пример данного проекта на www.pythonanywhere.com
Перейдите по ссылке, для просмотра действующего проекта 
www.zatomis.pythonanywhere.com
