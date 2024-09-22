FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

WORKDIR /frontend_api

RUN pip install --upgrade pip pipenv

COPY Pipfile Pipfile.lock /frontend_api/

RUN pipenv install --system --deploy

COPY . /frontend_api

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

