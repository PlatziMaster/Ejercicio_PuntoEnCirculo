#!/bin/bash

echo "=> Building image. It can take several minutes..."
echo "   running: docker-compose build -q"
echo ""
docker-compose build -q

echo "=> Creating executable script"
echo ""
chmod u+x run-app.sh

echo "=> Edit code locally and use 'run-app' command"
echo "   to execute the main script in the container"
echo ""
