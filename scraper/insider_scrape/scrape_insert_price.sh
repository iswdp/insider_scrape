cd ~/insider_scrape/scraper/insider_scrape
pipenv run ./index_scrape.py
pipenv run ./etf_scrape.py
pipenv run ./price_scrape.py
cd ~/insider-observer/
pipenv run ./manage.py shell < ./index_parse.py
pipenv run ./manage.py shell < ./etf_parse.py
pipenv run ./manage.py shell < ./single_price_parse.py