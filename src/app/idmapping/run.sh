#!/bin/bash
set -e
pip install -r /app/idmapping/requirements.txt
cd /app/idmapping/idmapping && gunicorn --reload -b 0.0.0.0:8000 app:app
