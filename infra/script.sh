#!/bin/bash

alembic upgrade head

#python3 main.py
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000