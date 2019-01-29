while true
do
cd ~/insider-observer/
pipenv run ./manage.py shell < ./single_price_parse.py
pipenv run ./manage.py shell < ./index_parse.py
pipenv run ./manage.py shell < ./etf_parse.py
done