exemplo1:
	@uvicorn exemplo-01:app --host 0.0.0.0 --port 8080 --reload

exemplo2:
	@uvicorn exemplo-02:app --host 0.0.0.0 --port 8080 --reload

run:
	@uvicorn app.app:app --host 0.0.0.0 --port 8080 --reload

install:
	@pip install -r requirements.txt