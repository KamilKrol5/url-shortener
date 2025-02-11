FROM python:3.11
WORKDIR /app
COPY pyproject.toml poetry.lock start-app.sh /app/

COPY src /app/src
RUN pip install --upgrade pip && pip install poetry --only main
RUN poetry install
COPY . /app/
EXPOSE 8005
ENTRYPOINT [ "poetry", "run", "/app/start-app.sh" ]