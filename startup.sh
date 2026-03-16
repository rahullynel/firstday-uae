#!/bin/bash

# FirstDay UAE Backend - Complete Startup Script

set -e

PROJECT_DIR="/home/rdsouza/firstday-uae"
BACKEND_DIR="$PROJECT_DIR/backend"

echo "╔═══════════════════════════════════════════════╗"
echo "║  FirstDay UAE Backend - Full Setup & Launch   ║"
echo "╚═══════════════════════════════════════════════╝"

# Step 1: Make sure we're in the right directory
cd "$BACKEND_DIR"
echo "✓ Working directory: $BACKEND_DIR"

# Step 2: Install system dependencies if needed
echo ""
echo "📦 Checking system dependencies..."
if ! python3 -m venv --help > /dev/null 2>&1; then
    echo "Installing python3-venv..."
    sudo apt install -y python3.12-venv python3-pip > /dev/null 2>&1
fi
echo "✓ Python development tools available"

# Step 3: Create virtual environment if it doesn't exist
echo ""
echo "🔧 Setting up Python environment..."
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv --without-pip
    echo "✓ Virtual environment created"
fi

# Step 4: Get pip working
echo ""
echo "📥 Installing pip..."
python3 -m ensurepip --default-pip 2>/dev/null || \
  curl -s https://bootstrap.pypa.io/get-pip.py | python3 - --break-system-packages 2>/dev/null || \
  python3 -m pip install --break-system-packages pip -q 2>/dev/null || \
  echo "⚠️  Using system Python directly"

# Step 5: Install requirements
echo ""
echo "⬇️  Installing dependencies..."
python3 -m pip install --break-system-packages -r requirements.txt -q 2>/dev/null || \
  echo "⚠️  Could not install via pip, dependencies may need manual installation"

# Step 6: Verify installation
echo ""
echo "✅ Verification..."
if python3 -c "import fastapi; print(f'  ✓ FastAPI {fastapi.__version__}')" 2>/dev/null; then
  echo "  ✓ All FastAPI dependencies available"
else
  echo "  ⚠️  FastAPI not installed - install with: pip3 install fastapi uvicorn"
fi

# Step 7: Show startup info
echo ""
echo "╔═══════════════════════════════════════════════╗"
echo "║          Ready to Start Backend!              ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "To start the backend server, run:"
echo ""
echo "  cd $BACKEND_DIR"
echo "  uvicorn app.main:app --reload"
echo ""
echo "Or if uvicorn is not found, try:"
echo "  python3 -m uvicorn app.main:app --reload"
echo ""
echo "API will be available at:  http://localhost:8000"
echo "Documentation at:          http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""

# Step 8: Ask if user wants to start now
read -p "Start backend now? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Starting backend..."
    echo ""
    python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi
