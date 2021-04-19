Update **config.py** with correct database information 

```
POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = ""
POSTGRES_DB = ""
```

Activate environment 

```
source venv/bin/activate
```

Install requirements.
```
pip install -r requirements.txt
```

Run migrations
```
chmod+x run-migrations.sh
./run-migrations.sh
```

Run flask
```
flask run
```

Run tests 

```
python -m unittest discover tests/unit/
```
