while true
do
cd ~/insider
source venv/bin/activate
cd scraper/insider_scrape/
./price_scrape.py
./index_scrape.py
./etf_scrape.py
deactivate
done