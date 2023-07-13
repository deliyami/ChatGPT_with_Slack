FROM python:3.10.11
ENV LANG C.UTF-8

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt; \
	apt-get update; \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    vim \
    ; \
    apt-get remove -y --auto-remove \
        wget \
        ; \
    rm -rf /var/lib/apt/lists/*;
COPY . /app

RUN ["python", "/app/main.py"]