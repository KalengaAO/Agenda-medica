# Agenda-medica

interview_TimeSaver
Sistema de gestão de agenda médica utilizando Flask, SQLite e Docker Compose.
Embora tenha começado por criar um docker-compose, 


### os conteiner serão testar manual.

docker run -it -p -v image 

root@organon:/home/org/Documents/Agenda-medica/project# docker exec -it flask bash

root@b657a9945b4c:/app/tools# printenv SECRET_KEY
123456789


root@organon:/home/org/Documents/Agenda-medica/project# docker exec -it flask bash

root@e0c8573fb0f3:/app/tools# apt-get update && apt-get install sqlite3

root@e0c8573fb0f3:/app/tools# cd  ../../

## testando sqlite

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

### testando a API
apt-get update && apt-get install iproute2 procps

root@b1f0b01f06e2:/app/tools# ss -ltn

State        Recv-Q       Send-Q              Local Address:Port                Peer Address:Port       
LISTEN       0            4096                   127.0.0.11:35155                    0.0.0.0:*          
LISTEN       0            2048                      0.0.0.0:5001                     0.0.0.0:*   


root@28842bd5df18:/app/tools# apt-get update && apt-get install curl

root@28842bd5df18:/app/tools# curl http://api:5001/agendamentos

[{"convenio":"Unimed","cpf":"123.456.789-00","data":"2026-07-25","especialidade":"Cardiologia","horario":"09:00","medico":"Dr. Jo\u00e3o Pereira","paciente":"Maria da Silva","status":"Confirmado"},{"convenio":"Bradesco Sa\u00fade","cpf":"987.654.321-00","data":"2026-07-25","especialidade":"Dermatologia","horario":"10:30","medico":"Dra. Ana Costa","paciente":"Jos\u00e9 Santos","status":"Aguardando confirma\u00e7\u00e3o"},{"convenio":"SulAm\u00e9rica","cpf":"456.789.123-00","data":"2026-07-26","especialidade":"Ortopedia","horario":"14:00","medico":"Dr. Paulo Mendes","paciente":"Carla Oliveira","status":"Confirmado"},{"convenio":"Particular","cpf":"321.654.987-00","data":"2026-07-26","especialidade":"Cl\u00ednico Geral","horario":"16:30","medico":"Dra. Fernanda Alves","paciente":"Roberto Lima","status":"Cancelado"},{"convenio":"Amil","cpf":"654.321.987-00","data":"2026-07-27","especialidade":"Cardiologia","horario":"08:00","medico":"Dr. Jo\u00e3o Pereira","paciente":"Juliana Rocha","status":"Confirmado"},{"convenio":"Unimed","cpf":"789.123.456-00","data":"2026-07-27","especialidade":"Dermatologia","horario":"11:15","medico":"Dra. Ana Costa","paciente":"Pedro Almeida","status":"Remarcado"},{"convenio":"Bradesco Sa\u00fade","cpf":"159.753.486-00","data":"2026-07-28","especialidade":"Ortopedia","horario":"13:45","medico":"Dr. Paulo Mendes","paciente":"Fernanda Souza","status":"Confirmado"},{"convenio":"Particular","cpf":"753.159.486-00","data":"2026-07-28","especialidade":"Cl\u00ednico Geral","horario":"17:00","medico":"Dra. Fernanda Alves","paciente":"Lucas Martins","status":"Aguardando confirma\u00e7\u00e3o"}]





## Execução do projeto

### Pré-requisitos

Certifique-se de ter instalado:

- Docker
- Docker Compose
- Make  : sudo apt install -y git make

Verifique:

```bash
docker --version
docker compose version
make --version