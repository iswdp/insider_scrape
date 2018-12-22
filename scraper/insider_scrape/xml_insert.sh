while true
do
cd ~/insider-observer/
pipenv run ./manage.py shell < ./xml_parse.py
done
