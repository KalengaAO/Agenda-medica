# Agenda-medica

interview_TimeSaver

Embora tenha começado por criar um docker-compose, 


os conteiner serão testar manual.

docker run -it -p -v image 

root@organon:/home/org/Documents/Agenda-medica/project# docker exec -it flask bash

root@b657a9945b4c:/app/tools# printenv SECRET_KEY
123456789


root@organon:/home/org/Documents/Agenda-medica/project# docker exec -it flask bash

root@e0c8573fb0f3:/app/tools# apt-get update && apt-get install sqlite3

root@e0c8573fb0f3:/app/tools# cd  ../../

root@e0c8573fb0f3:/# sqlite3 data/agenda.db 
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.

sqlite> .tables
usuarios

sqlite> SELECT password_hash FROM usuarios;
scrypt:32768:8:1$xD2Pk5RR23VQ1WM0$0000000000000000000000

sqlite> SELECT id, username, email FROM usuarios;
1|medico.teste|medico.teste@timesaver.com.br


root@organon:/home/org/Documents/Agenda-medica/project# docker exec -it api bash

testando a API
apt-get update && apt-get install iproute2 procps

root@b1f0b01f06e2:/app/tools# ss -ltn

State        Recv-Q       Send-Q              Local Address:Port                Peer Address:Port       
LISTEN       0            4096                   127.0.0.11:35155                    0.0.0.0:*          
LISTEN       0            2048                      0.0.0.0:5001                     0.0.0.0:*   
