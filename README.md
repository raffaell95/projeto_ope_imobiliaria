# projeto_ope_imobiliaria

Projeto de um sistema para imobiliária com django

Projeto rodando no heroku: https://projeto-ope-imob.herokuapp.com/


## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/raffaell95/projeto_ope_imobiliaria.git
cd projeto_ope_imobiliaria
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
