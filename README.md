[![Build Status](https://travis-ci.org/rafaelhenrique/wttd.svg?branch=master)](https://travis-ci.org/rafaelhenrique/wttd)
# Eventex

Eventex is a project of course Welcome to the Django (welcometothedjango.com.br) by Henrique Bastos.

## How to dev?

1. Clone repo
2. Create virtualenv with python 3.5
3. Activate virtualenv
4. Install requirements
5. Configure environment with .env
6. Run tests

```console
git clone git@github.com:rafaelhenrique/wttd.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## How to Deploy?

1. Create instance into heroku
2. Send configuration to heroku
3. Create an secure SECRET_KEY to instance
4. Define DEBUG=False
5. Configure email service
6. Send code to heroku

```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure the email
git push heroku master --force
```

* Im not have internet not.. then i add contrib/secret_gen.py another time

## Demo

[https://eventex-rafaelhenrique.herokuapp.com/](https://eventex-rafaelhenrique.herokuapp.com/)
