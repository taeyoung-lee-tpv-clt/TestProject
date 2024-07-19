ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

RUN mkdir -p /app/
RUN mkdir -p /app/logs

# COPY ./apps /app/apps
COPY ../common /app/common
COPY ../config /app/config
# COPY ./proto /app/proto
# COPY ./service_account_key /app/service_account_key 내껄로 하기
COPY ../utility /app/utility
COPY ../redis_common /app/redis_common
COPY ../main.py /app/main.py
COPY ../shell_script/run_dev.sh /app/run_main.sh
# COPY ../submodules /app/submodules
COPY ../requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD ["bash", "./run_main.sh"]

