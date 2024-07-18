ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

RUN mkdir -p /app/
RUN mkdir -p /app/logs

# COPY ./apps /app/apps
COPY ./RedProject/common /app/common
COPY ./RedProject/config /app/config
# COPY ./proto /app/proto
# COPY ./service_account_key /app/service_account_key 내껄로 하기
COPY ./RedProject/utility /app/utility
COPY ./RedProject/main.py /app/main.py
COPY ./RedProject/shell_script/run_dev.sh /app/run_main.sh
COPY ./RedProject/submodules /app/submodules
COPY ./RedProject/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app
CMD ["bash", "./run_main.sh"]