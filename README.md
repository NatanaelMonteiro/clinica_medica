# Clinica Médica


Proposta de controle de uma clínica médica, usando html (htmx) e css no frontend e python (fastapi), sqlite/postgres no backend.


## Pré-requisitos

Python 3.x

Sqlite

Postgres

HTML

CSS

JavaScript


## Como instalar no Windows


git clone https://github.com/NatanaelMonteiro/clinica_medica.git

cd clinica_medica

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload


## Acesso

Usuário: diego@professor.com

Senha: nota10


## Povoar tabelas de agendamento e cancelamento de consulta

Realizar dentro do app


## Observação

No linux, se der erro na instalação da lib psycopg2, provavelmente falta instalar as de build. Instlar com os comandos:

sudo apt install libpq-dev python3.x-dev (onde x depende da versão python3 usado por você)

sudo apt install build-essential.

pip install -r requirements.txt

python db_init.py

uvicorn main:app

