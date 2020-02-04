FROM node
RUN mkdir /app
COPY . /app
WORKDIR /app/frontend

RUN npm install
RUN npm run production

FROM python:3.8
WORKDIR /app
COPY --from=0 /app .
RUN pip install pipenv
RUN pipenv install  --system --deploy --ignore-pipfile
