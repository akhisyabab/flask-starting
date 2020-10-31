source venv/bin/activate
source scripts/prod_env.sh
flask db upgrade
nohup flask run -h 0.0.0.0 -p 80 >/dev/null 2>&1 &