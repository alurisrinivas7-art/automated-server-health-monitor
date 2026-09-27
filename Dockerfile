FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY src/ ./src/


FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --from=builder /app/src ./src

# Remove build-time package manager from the runtime image
RUN rm -rf \
    /usr/local/lib/python3.14/site-packages/pip \
    /usr/local/lib/python3.14/site-packages/pip-*.dist-info \
    /usr/local/bin/pip \
    /usr/local/bin/pip3 \
    /usr/local/bin/pip3.14

CMD ["python", "-m", "src.monitor"]
