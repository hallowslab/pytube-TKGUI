FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN set -xe && apt update && apt install -y \
  git sudo wget curl build-essential libssl-dev openssl \
  software-properties-common lzma-dev tk-dev \
  gdb lcov pkg-config uuid-dev zlib1g-dev lzma  \
  libbz2-dev libffi-dev libgdbm-dev liblzma-dev \
  libncurses5-dev libreadline6-dev libsqlite3-dev

RUN sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && sed -i -- 's/# deb-src/deb-src/g' /etc/apt/sources.list
RUN apt update && apt build-dep -y python3

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
RUN ./configure --enable-optimizations --enable-shared
RUN make -j2
RUN make install


# pytube_tkgui - project #
WORKDIR /home/proj
COPY ./ /home/proj
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# Permanently export the path for bash
ENV PATH="$PATH:$HOME/.local/bin"
# Install python project dependencies
RUN $HOME/.local/bin/poetry install

RUN $HOME/.local/bin/poetry run task build

ENTRYPOINT [ "/bin/bash" ]