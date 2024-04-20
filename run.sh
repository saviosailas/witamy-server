source .env
python -m flask --app witamy_server create-database
python -m flask --app=witamy_server run --debug