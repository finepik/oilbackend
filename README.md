# Учебный проект - сайт для продажи масла (e-commers)

Проект сайта по продаже масла включает в себя каталоги продукции и лендинг. 

Основная цель сайта — предоставить пользователям удобный интерфейс для просмотра и покупки различных видов масла.

Backend сайта разработан с использованием Django, библиотек Django REST Framework, pillow, simplejwt.

СУБД: postgreSQL.

## Описание

**Главная страница сайта**

![image](https://github.com/user-attachments/assets/09c08632-1a18-4647-81f3-342bb1ef9ad2)

**Страница о продукте**

![image](https://github.com/user-attachments/assets/ad4ab7fd-7e99-470e-8cff-998651873feb)

**Страница каталога**

![image](https://github.com/user-attachments/assets/bff99a7a-4142-454d-94d1-b4f841e506a8)

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/finepik/oilbackend.git
   cd Shop
   ```
2. **Установите зависимости**
    ```bash
    pip install -r requirements.txt
    ```
3. **Примените миграции:**
   ```bash
   cd Shop
   python manage.py migrate
   ```
4. **Запустите сервер**
    ```bash
    python manage.py runserver
    ```

## Использование
После запуска сервера вы сможете получить доступ к приложению по адресу:
- Django API: http://localhost:8000/
