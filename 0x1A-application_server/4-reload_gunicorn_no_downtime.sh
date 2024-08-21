#!/bin/bash

# Get the PID of the master Gunicorn process
MASTER_PID=$(pgrep -f 'gunicorn.*web_flask.0-hello_route:app')

# Check if the master process is found
if [ -z "$MASTER_PID" ]; then
    echo "Gunicorn master process not found."
    exit 1
fi

# Send the HUP signal to the master process to gracefully reload workers
kill -HUP $MASTER_PID

echo "Gunicorn is reloading gracefully."
