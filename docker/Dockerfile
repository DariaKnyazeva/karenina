# -*- mode: conf -*-
FROM phusion/baseimage

ENV DB_USER viewsite
ENV DB_PASSWORD viewsite
ENV DB_NAME viewsite

USER root
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN /usr/sbin/enable_insecure_key


# Common tools

RUN \
  apt-get update && \
  apt-get install -y build-essential git


# Node.js tools

RUN \
  apt-get install -y nodejs nodejs-legacy npm && \
  npm install -g grunt-cli bower


# Python

RUN apt-add-repository -y ppa:fkrull/deadsnakes
RUN apt-get update

RUN apt-get install -y python2.6 python2.6-dev \
    python2.7 python2.7-dev python3.3 python3.3-dev \
    python3.4 python3.4-dev python-virtualenv python-tox


# PostgeSQL
# https://github.com/orchardup/docker-postgresql

RUN \
  apt-get install -y postgresql-9.3 postgresql-client-9.3 libpq-dev python-psycopg2 python3-psycopg2 && \
  \
  POSTGRESQL_BIN=/usr/lib/postgresql/9.3/bin/postgres; \
  POSTGRESQL_CONFIG_FILE=/etc/postgresql/9.3/main/postgresql.conf; \
  POSTGRESQL_SINGLE="sudo -u postgres $POSTGRESQL_BIN --single --config-file=$POSTGRESQL_CONFIG_FILE"; \
  echo "CREATE USER $DB_USER WITH SUPERUSER;" | $POSTGRESQL_SINGLE && \
  echo "ALTER USER $DB_USER WITH PASSWORD '$DB_PASSWORD';" | $POSTGRESQL_SINGLE && \
  echo "CREATE DATABASE $DB_NAME OWNER $DB_USER TEMPLATE DEFAULT;" | $POSTGRESQL_SINGLE && \
  \
  sed -i 's/^local\s\+all\s\+all\s\+peer/local all all md5/g' /etc/postgresql/9.3/main/pg_hba.conf && \
  echo "host all all 0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf && \
  echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf && \
  \
  echo "fsync = off" >> /etc/postgresql/9.3/main/postgresql.conf

RUN mkdir /etc/service/postgresql
ADD postgresql.sh /etc/service/postgresql/run

VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
EXPOSE 5432


# User profile setup

RUN \
  useradd -d /home/viewsite -m -s /bin/bash viewsite && \
  echo viewsite:viewsite | chpasswd && \
  echo 'sensu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/viewsite && \
  chmod 0440 /etc/sudoers.d/viewsite && \
  mkdir -p /home/viewsite/.ssh && \
  cat ~/.ssh/authorized_keys > /home/viewsite/.ssh/authorized_keys && \
  chown -R viewsite:viewsite /home/viewsite/.ssh && \
  echo "cd /srv/viewsite" >> /home/viewsite/.bashrc


# Finalizing  baseimage-docker's

CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Project setup

EXPOSE 8000

