#!/bin/sh

set -e

mkdir -p /run/mysqld

chown -R mysql:mysql /run/mysqld
chown -R mysql:mysql /var/lib/mysql

if [ ! -d "/var/lib/mysql/mysql" ]; then

    mariadb-install-db \
        --user=mysql \
        --datadir=/var/lib/mysql

    mysqld \
        --user=mysql \
        --skip-networking &

    pid="$!"

    until mariadb-admin ping --silent
    do
        sleep 1
    done

    mariadb < /init.sql

    mariadb-admin shutdown

    wait "$pid"

fi

exec mysqld --user=mysql