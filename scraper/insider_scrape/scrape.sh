while true
do
cd ~/insider_scrape/scraper/insider_scrape
pipenv run scrapy crawl links
pipenv run scrapy crawl full
pipenv run ./filter_ownership_docs.py
done