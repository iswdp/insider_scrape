cd ~/insider
source venv/bin/activate
cd scraper/insider_scrape
scrapy crawl links
scrapy crawl full
./filter_ownership_docs.py
deactivate
cd ~/insider_django/insider/
pipenv run ./manage.py shell < ./xml_parse.py