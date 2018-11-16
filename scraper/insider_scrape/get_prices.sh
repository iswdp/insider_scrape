while true
do
cd ~/insider
source venv/bin/activate
cd scraper/insider_scrape/
./price_scrape.py
./index_scrape.py
./etf_scrape.py
deactivate
cd ~/insider-observer/
pipenv run ./manage.py shell < ./single_price_parse.py
pipenv run ./manage.py shell < ./index_parse.py
pipenv run ./manage.py shell < ./etf_parse.py
done