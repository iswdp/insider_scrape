while true
do
cd ~/insider
source venv/bin/activate
cd scraper/insider_scrape/
./price_scrape.py
deactivate
cd ~/insider-observer/
pipenv run ./manage.py shell < ./single_price_parse.py
done