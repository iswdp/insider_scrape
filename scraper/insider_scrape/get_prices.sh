while true
do
cd ~/insider_scrape/scraper/insider_scrape
pipenv run ./index_scrape.py
pipenv run ./etf_scrape.py
pipenv run ./price_scrape.py
done