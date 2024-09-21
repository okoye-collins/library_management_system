FROM python:3.10.12
ENV PYTHONUNBUFFERED 1

WORKDIR /backend_api

RUN pip install --upgrade pip pipenv

COPY Pipfile Pipfile.lock /backend_api/

RUN pipenv install --system --deploy

COPY . /backend_api

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
