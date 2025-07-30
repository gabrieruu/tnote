FROM python:bullseye

RUN apt-get update && \
	apt-get install -y fzf && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash dev

WORKDIR /home/dev/tnote
RUN chown -R dev:dev /home/dev/tnote

USER dev
