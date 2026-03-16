#!/bin/bash

# FirstDay UAE Backend - Local Development Setup

set -e

echo "🚀 FirstDay UAE Backend - Local Setup"
echo "======================================"

# Check Python
echo "✓ Python $(python3 --version | cut -d' ' -f2)"

# Check if venv is available
if ! python3 -m venv --help > /dev/null 2>&1; then
    echo ""
    echo "❌ Python venv module not found."
    echo ""
    echo "On Ubuntu/Debian, install it with:"
    echo "  sudo apt install python3.12-venv python3-pip"
    echo ""
    exit 1
fi

# Check if venv already exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✓ Virtual environment already exists"
fi

# Activate venv
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the backend server, run:"
echo "  cd backend"
echo "  source .venv/bin/activate"
echo "  uvicorn app.main:app --reload"
echo ""
echo "API will be available at http://localhost:8000"
echo "Documentation at http://localhost:8000/docs"
