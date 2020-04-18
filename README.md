# django_base
Basic template for django projects.

# Virtualenv

Install and activate
```sh
virtualenv -p python3 venv
source venv/bin/activate
```

Run requirements.txt
```sh
pip3 install -r requirements.txt
```

# Settings

To handle with differents stages of deploy/testing... uncouple `settings.py` in this way.


o
`-- django_base
    `-- django_base      -> config
        `-- settings.py  -> settings/
            |-- base.py
            |-- local.py
            |-- staging.py
            `-- production.py


# .env

In order to use volatile configs, use the .env enviroment with the structure

```
KEY=SOME_VALUE
KEY=SOME_OTHER_VALUE
```

# Databases
if you are using write/read databases, use

# AWS
The django storages
call aws settings import


# Notes

If you are using mongo.db and djongo, consider override the requierements.txt