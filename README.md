```
source shortyenv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver

python3 -m pip list --format=freeze

mysql -u root
```