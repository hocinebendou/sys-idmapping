#!/bin/bash
set -e
export APP_SETTINGS=config.ProductionConfig
cd /app/idmapping/ && gunicorn --reload -b 0.0.0.0:8000 app:app
