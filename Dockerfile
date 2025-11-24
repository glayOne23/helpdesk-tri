# ============================
#            Builder
# ============================
FROM python:3.10-slim AS builder

ENV DockerHOME=/home/app/webapp
WORKDIR $DockerHOME

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc libpq-dev postgresql-client \
    python3-dev default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies first for proper layer caching
COPY ./docs/requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# ============================
#         Runtime
# ============================
FROM python:3.10-slim

ENV DockerHOME=/home/app/webapp
WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq-dev default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy project source
COPY ./project $DockerHOME

# CMD gunicorn or runserver later
