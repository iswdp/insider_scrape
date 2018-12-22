while true
do
cd ~/insider
source venv/bin/activate
cd scraper/insider_scrape
scrapy crawl links
scrapy crawl full
./filter_ownership_docs.py
deactivate
done