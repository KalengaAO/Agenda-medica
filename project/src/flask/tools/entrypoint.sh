#! /bin/sh

set -e 
echo "aguardando mariadb"

until nc -z mairiadb 3306; do
    sleep 1
done

echo "mariadb está pronto"

exec $@