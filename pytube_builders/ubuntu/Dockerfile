FROM ubuntu:16.04

RUN set -xe && apt update && apt install -y \
  git python-is-python3 python3 python3-pip \
  python3-venv

SHELL ["/bin/bash", "-c"]

# pytube_tkgui - project #
WORKDIR /home/pytube_tkgui
COPY ./ /home/pytube_tkgui
# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/pytube_tkgui/.poetry python3 -
# Permanently export the path for bash
ENV PATH="$PATH:/home/pytube_tkgui/pymap/.poetry/bin"
# Install python project dependencies
RUN poetry install

RUN poetry run task build