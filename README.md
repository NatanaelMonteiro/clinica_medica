# Clinica Médica


Proposta de controle de uma clínica médica, usando html (htmx) e css no frontend e python (fastapi), sqlite/postgres no backend.


## Como instalar no Windows


git clone https://github.com/NatanaelMonteiro/clinica_medica.git

cd clinica_medica

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload



## Como instalar no Linux


git clone https://github.com/NatanaelMonteiro/clinica_medica.git

cd clinica_medica

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python -m uvicorn main:app --reload