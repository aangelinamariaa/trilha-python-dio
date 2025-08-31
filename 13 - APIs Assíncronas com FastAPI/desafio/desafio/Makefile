run:
	@uvicorn workout_api.main:app --reload

create-migration:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "init_db"

run-migration:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head