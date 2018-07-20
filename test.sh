#!/usr/bin/env bash


clear
echo "Running ProjectName ..."
if [ ! -f "master.db" ]; then
    echo "Creating database from schema ..."
    python3 run/core/setup/schema.py
    python3 run/core/setup/seed.py
fi
echo "Database loaded ..."
echo "Launching ProjectName test server ..."
python3 run/wsgi.py