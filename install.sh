#!/bin/bash
PROGNAME=$(basename $0)
echo 'Install BIBBOX SYS-ID MAPPING Microservice'
echo '-  Create data folder for redis'

mkdir -p data/redis/data

echo '-  Finished'
echo 'add a proxy for the port 8051'
echo 'run docker-compose up -d'