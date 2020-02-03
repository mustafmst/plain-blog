FROM node
WORKDIR /root
COPY . .
WORKDIR /root/frontend

RUN npm install
RUN npm run production

FROM python:3.8
WORKDIR /root
RUN pip install pipenv
RUN pipenv install
CMD ["python","manage.py","runserver"]
