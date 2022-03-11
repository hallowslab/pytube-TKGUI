FROM ubuntu:16.04

RUN set -xe && apt update && apt install -y \
  git sudo wget curl build-essential libssl-dev openssl \
  software-properties-common python-software-properties \
  gdb lcov pkg-config uuid-dev zlib1g-dev lzma lzma-dev tk-dev \
  libbz2-dev libffi-dev libgdbm-dev liblzma-dev \
  libncurses5-dev libreadline6-dev libsqlite3-dev


RUN sudo apt-get build-dep python3

SHELL ["/bin/bash", "-c"]
RUN adduser --disabled-password --gecos '' proj
RUN adduser proj sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN sudo chown -R proj:proj /home

# Build python 3.8.10 from source
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
RUN tar xzvf Python-3.8.10.tgz
WORKDIR /opt/Python-3.8.10
RUN ./configure --enable-optimizations
RUN make
RUN make install


USER proj
# pytube_tkgui - project #
WORKDIR /home/proj
COPY ./ /home/proj
# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/proj/.poetry python3 -
# Permanently export the path for bash
ENV PATH="$PATH:/home/proj/.poetry/bin"
# Install python project dependencies
RUN poetry install

RUN poetry run task build