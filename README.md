# Math-Proof-REST-API

pip install -r requirements/dev.txt
createdb -U postgres openstax
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
