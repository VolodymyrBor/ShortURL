FROM python:3.9.2-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN apt-get update && apt-get install -y \
	dumb-init --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN useradd --create-home short_url_user
WORKDIR /home/short_url_user
USER short_url_user

COPY . .

CMD Makefile create-tables

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD uvicorn runserver:app --host 0.0.0.0 --port 8000
