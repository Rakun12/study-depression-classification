FROM python:3.12-slim-bullseye

RUN pip install pipenv 

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model/dv n model.bin", "./"]

EXPOSE 1212

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1212", "predict:app"]