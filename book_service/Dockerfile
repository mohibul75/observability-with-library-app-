ARG PYTHON_VERSION=3.10.12-alpine3.18
FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED=1
WORKDIR /wheels
RUN apk add --update --no-cache \
    alpine-sdk \
    postgresql-dev \
    openssl-dev \
    libffi-dev \
    python3-dev
RUN apk add --no-cache --update python3 py3-pip
COPY requirements.txt .
RUN pip wheel -r requirements.txt --disable-pip-version-check

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache \
    libpq \
    postgresql-client
COPY --from=builder /wheels /wheels
RUN pip install \
        --no-cache-dir \
        --disable-pip-version-check \
        -r /wheels/requirements.txt \
        -f /wheels \
    && rm -rf /wheels
WORKDIR /app
COPY . .
COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh
EXPOSE 8000
ENTRYPOINT [ "/app/entrypoint.sh" ]