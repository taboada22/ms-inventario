FROM python:3.10-slim-bullseye

ENV FLASK_CONTEXT=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

RUN useradd --create-home --home-dir /home/flaskapp flaskapp
RUN apt-get update
RUN apt-get install -y python3-dev build-essential libpq-dev python3-psycopg2
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*


WORKDIR /home/flaskapp/app

COPY  . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD [ "python", "./app.py" ]