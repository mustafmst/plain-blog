# Plain Blog

Simple, plain blog webapp written with django and vue.js.

## Local development setup

1. Create `.env` file in root directory
2. Put in it this values:
    ```
    DEBUG=True
    ALLOWED_HOSTS=localhost
    ```
3. Run `pipenv install`
4. Go to `frontend` dir
5. Run `npm i`
6. For building frontend run `npm run watch` in `frontent` dir
7. For server run: `python manage.py runserver` in project root dir

## Running localy(Docker)

Just use `docker-compose up` in project root dir.