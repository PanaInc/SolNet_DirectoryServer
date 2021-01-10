echo python-3.7.8 > runtime.txt 
pip freeze > requirements.txt

echo web: gunicorn /src/app:app > Procfile

git push heroku main

heroku open