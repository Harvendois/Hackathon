EXPORT = export PYTHONPATH=$(PWD)
include .env

db:
	psql -c "DROP DATABASE IF EXISTS igotcareer_db"
	#psql -c "DROP ROLE IF EXISTS flanb"
	#psql -c "CREATE USER flanb WITH SUPERUSER PASSWORD 'fb0109##'"
	psql -c "CREATE DATABASE igotcareer_db OWNER flanb"


upgrade:
	$(EXPORT) && pipenv run alembic upgrade head

downgrade:
	$(EXPORT) && pipenv run alembic downgrade head

drop-test-db:
	$(EXPORT) && pipenv run sh scripts/remove_local_test_dbs.sh
