#!/bin/bash

# Simple runner for FirstDay UAE Backend using pip3
# Run this script to start the backend:
# bash run-backend.sh

cd /home/rdsouza/firstday-uae/backend

echo "🚀 FirstDay UAE Backend - Starting..."
echo ""

# Try different ways to run the server
if command -v pip3 &> /dev/null && pip3 show fastapi &> /dev/null; then
    echo "✓ Using pip3-installed FastAPI"
    python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
elif python3 -c "import fastapi; print('✓ FastAPI found')" 2>/dev/null; then
    echo "✓ FastAPI available in Python"
    python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
else
    echo "⚠️  FastAPI not found, installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
    echo "✓ Dependencies installed, starting server..."
    python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi
