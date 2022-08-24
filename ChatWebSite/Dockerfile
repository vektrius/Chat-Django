FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]