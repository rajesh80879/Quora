# Quora Clone

A Django-based Quora-inspired web application where users can register, post questions, answer them, and like answers.

---

## Tech Stack
- Python 3.x
- Django 4.x
- PostgreSQL / MySQL / SQLite (Based on your choice)
- Bootstrap 5 (Frontend Styling)

---

## Steps to Setup and Run Django Project

1. Clone the repository: `git clone https://github.com/rajesh80879/catalyst.git`
2. Create a python env and activate 
3. Install dependencies: `pip install -r requirements.txt`
4. Make migration:  `python manage.py makemigrations core`
5. Migrate:  `python manage.py migrate`
6. Run the project:  `python manage.py runserver`

## Database and env setup

- Create an `.env` file in the `catalyst_count` folder.

- Add the following configuration variables to the `.env` file:

    ```plaintext
    SECRET_KEY=django-insecure-bp$owpv1yj4g1#pg3u^(kp#&qxm(-4+&kpv#0co0-)5k@&bv70
    DEBUG=True
    ALLOWED_HOSTS=*


    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_NAME='your-database-name'
    DATABASE_USER='db-user'
    DATABASE_PASSWORD='db-password'
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

- Alternatively, you can use SQLite as the database. Uncomment the following configuration in the `settings.py` file:

    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    ```
